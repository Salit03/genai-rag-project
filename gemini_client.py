import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

_client = None

GEMINI_MODEL = "gemini-3.1-flash-lite"

MAX_ATTEMPTS = 3
INITIAL_WAIT = 2


def get_client():
    global _client

    if _client is None:

        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. "
                "Make sure your .env file contains GEMINI_API_KEY."
            )

        _client = genai.Client(
            api_key=api_key
        )

    return _client


def _is_retryable(error):

    error_str = str(error).lower()

    return any(k in error_str for k in [
        "503",
        "429",
        "timeout",
        "unavailable",
        "500",
        "internal",
        "connection"
    ])


def _call_gemini(
    prompt,
    temperature=0.7,
    max_tokens=1024,
    system=None
):

    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
        system_instruction=system
    )

    for attempt in range(MAX_ATTEMPTS):

        try:

            client = get_client()

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config=config
            )

            return response.text

        except Exception as e:

            print("Request failed:", e)

            if not _is_retryable(e):
                raise

            if attempt == MAX_ATTEMPTS - 1:
                raise

            wait = INITIAL_WAIT * (2 ** attempt)

            print(
                f"Request failed. Retrying in {wait} seconds..."
            )

            time.sleep(wait)

def generate_with_metadata(
    prompt ,
    temperature=0.7,
    max_tokens=1024,
    system=None
):
    client = get_client()
    config = types.GenerateContentConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
        system_instruction=system
    )
    response= client.models.generate_content(
        model = GEMINI_MODEL,
        contents = prompt,
        config = config
    )
    return {
        "text": response.text,
        "input_tokens": response.usage_metadata.prompt_token_count,
        "output_tokens": response.usage_metadata.candidates_token_count,
        "total_tokens": response.usage_metadata.total_token_count,
        "finish_reason": str(response.candidates[0].finish_reason),
    }

def generate(
    prompt,
    temperature=0.7,
    max_tokens=1024,
    system=None
):

    return _call_gemini(
        prompt,
        temperature,
        max_tokens,
        system
    )

## Testing / direct execution code
if __name__ == "__main__":

    answer = generate_with_metadata(
        "Explain RAG in one simple sentence."
    )

    print(answer)