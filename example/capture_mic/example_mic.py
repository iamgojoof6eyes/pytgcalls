from pyrogram import Client

from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls import idle
from pytgcalls.media_devices import MediaDevices
from pytgcalls.types import CaptureAudioDevice

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
call_py.join_group_call(
    -1001234567890,
    CaptureAudioDevice(
        MediaDevices.get_audio_devices()[0],
    ),
    stream_type=StreamType().pulse_stream,
)
idle()
