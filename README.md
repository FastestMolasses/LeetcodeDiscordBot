# Leetcode Discord Bot
Sends daily problem to a Discord channel. Tested on Python 3.10.

![python](https://github.com/FastestMolasses/LeetcodeDiscordBot/actions/workflows/main.yaml/badge.svg)

## Installation

1. Setup a Python environment

    ```bash
    $ python -m venv env
    ```

2. In VSCode, make sure you set this environment as the default Python interpreter. This can also be done by pressing `cmd/ctrl + shift + P` and typing ">Python: Select Interpreter", then selecting the newly created environment `./env/bin/python`

3. Enter the environment if you haven't already

    ```bash
    # macOS
    $ source env/bin/activate
    # windows
    $ .\env\Scripts\activate
    ```

4. Install requirements

    ```bash
    $ pip install -r requirements.txt
    ```

5. Rename `.env.sample` to `.env` and fill out the required credentials

6. Run main.py
