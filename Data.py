from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can extract text from images using OCR technology.

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏠Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/m2botz/17")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About😎", callback_data="about")
        ],
        [InlineKeyboardButton("Updates Channel", url="https://t.me/m2botz")],
        [InlineKeyboardButton("Support Group", url="https://t.me/m2botzsupport")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by joining @m2botz.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @m2botz

Updates Channel : [Click Here](https://t.me/m2botz)

Support : [Click Here](https://t.me/m2botzsupport)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [M2](https://t.me/ask_admin01)
    """
