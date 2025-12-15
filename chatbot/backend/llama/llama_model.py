import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llama(prompt: str) -> str:
    print("\n⏳ Thinking...\n")

    payload = {
        "model": "llama3.2",   # must match `ollama list`
        "prompt": prompt,
        "stream": True        # 🔴 IMPORTANT
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            stream=True,        # 🔴 IMPORTANT
            timeout=120
        )

        if response.status_code != 200:
            return f"❌ LLaMA HTTP error: {response.text}"

        final_text = ""

        # Read streamed chunks line-by-line
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    final_text += data["response"]
                if data.get("done", False):
                    break

        return final_text.strip()

    except requests.exceptions.Timeout:
        return "⚠️ LLaMA timed out. Please try again."

    except Exception as e:
        return f"❌ LLaMA exception: {str(e)}"
