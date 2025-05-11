import dotenv
import os
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent
from deepgram import DeepgramClient
from utils import get_audio_output_path

mcp = FastMCP("Deepgram MCP")

dotenv.load_dotenv()
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

deepgram = DeepgramClient(DEEPGRAM_API_KEY)


@mcp.tool(
        description="Convert text to speech using Deepgram API",
)
def text_to_speech(text: str):
    """Converts a text to speech and returns the audio
    Cost Warning: This tool is paid and will can cost you deepgram credits.
    """
    filename = get_audio_output_path()
    SPEAK_TEXT = {
        "text": text,
    }
    response = deepgram.speak.rest.v("1").save(str(filename), SPEAK_TEXT)
    print(response.to_json(indent=4))
    return TextContent(
        type="text",
        text=f"Success. File saved as: {filename}.",
    )

@mcp.tool(
        description="Play the audio file using afplay",
)
def play_audio(path: str):
    """Plays the audio file."""
    if not os.path.exists(path):
        return TextContent(
            type="text",
            text=f"File {path} does not exist.",
        )
    os.system(f"afplay {path}")
    return TextContent(
        type="text",
        text=f"Playing audio file: {path}.",
    )


if __name__ == "__main__":
    mcp.run(transport='stdio')