# Discord Activity Changer

A small Python script that sets a custom Discord Rich Presence activity for **Where Winds Meet**. It keeps the activity active until you stop the script.

## Requirements

- Python 3
- The Discord desktop app, running and signed in
- A Discord application and its Application ID

## Setup

1. Clone this repository and open its folder in a terminal.
2. Install the dependency with `python -m pip install pypresence`.

3. In `main.py`, replace `CLIENT_ID` with the full Application ID from your app's **General Information** page in the [Discord Developer Portal](https://discord.com/developers/applications). The sample value must be replaced before running.

## Run

```sh
python main.py
```

The script publishes the activity with the state `In Game` and the detail `Playing Where Winds Meet`. Press `Ctrl+C` in the terminal to stop it. This sets a Rich Presence activity; it does not detect whether the game is actually running.

## Troubleshooting

- **Discord is not running:** Start the Discord desktop app and run the script again. The browser version is not sufficient for local Rich Presence.
- **Invalid Application ID:** Copy the Application ID from the Discord Developer Portal and check the `CLIENT_ID` value in `main.py`.

Do not put a Discord bot token or application client secret in this script or in a public repository. Only the Application ID is needed for this project.
