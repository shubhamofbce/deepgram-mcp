import uuid
from pathlib import Path

def get_audio_output_path() -> Path:
    """Utility to get the output path for audio files, ensuring the directory exists."""
    output_dir = Path.home() / "Desktop" / "deepgram" / "audio"
    output_dir.mkdir(parents=True, exist_ok=True)
    uuid4_str = str(uuid.uuid4())
    return output_dir / f"output_{uuid4_str}.mp3"