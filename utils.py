from dotenv import load_dotenv
import base64

load_dotenv()


def converting_code64(client_id: str, client_secret: str) -> str:
    string = client_id + ":" + client_secret
    string_bytes = string.encode("utf-8")
    base64_bytes = str(base64.b64encode(string_bytes), "utf-8")
    return base64_bytes
