import os


class Config:

    BOT_TOKEN = "6059453194:AAHvwYfK3sen6fok5DKe83M6jz1C7SCzcrg"

    SESSION_NAME = ":memory:"

    API_ID = 2943728

    API_HASH = "f92341ae32e29aa1bfdf3b5a5d25a80a"

    CLIENT_ID = "1005570709419-6k5es908759kn9up85pm43sh47ft4tpv.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = 535883227

    AUTH_USERS_TEXT = "535883227"

    AUTH_USERS = [BOT_OWNER] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
