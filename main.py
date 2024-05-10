{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMrArkyzye9iu5ZzLyu0GHS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aniishap/ds2002/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TaPMVV4lf5oc"
      },
      "outputs": [],
      "source": [
        "from typing import Final\n",
        "import os\n",
        "from dotenv import load_dotenv\n",
        "from discord import Intents, Client, Message\n",
        "from responses import get_response, guess_rank\n",
        "\n",
        "# Step 0: load our token from somewhere safe\n",
        "load_dotenv()\n",
        "Token: Final[str] = os.getenv('DISCORD_TOKEN')\n",
        "\n",
        "# Step 1: BOT SETUP Without intents your bot won't respond\n",
        "intents: Intents = Intents.default()\n",
        "intents.message_content = True\n",
        "client: Client = Client(intents=intents)\n",
        "\n",
        "# track user responses\n",
        "user_responses = {}\n",
        "\n",
        "\n",
        "# Step 2: Message Function\n",
        "async def send_message(message: Message, user_message: str) -> None:\n",
        "    if not user_message:\n",
        "        print('(Message was empty because intents were not enabled ... probably)')\n",
        "        return\n",
        "    try:\n",
        "        if message.author in user_responses:\n",
        "            await handle_existing_response(message)\n",
        "        else:\n",
        "            await handle_new_response(message, user_message)\n",
        "    except Exception as e:\n",
        "        print(f'There has been an error: {e}')\n",
        "\n",
        "\n",
        "# Step 3: Handle user response to previous prompt\n",
        "async def handle_existing_response(message: Message) -> None:\n",
        "    correct_answer = user_responses[message.author]['answer']\n",
        "    # check if user answer matches correct answer\n",
        "    user_message = message.content.strip()\n",
        "    if user_message == correct_answer:\n",
        "        await message.channel.send(f\"Correct! It is: \\n{correct_answer}\")\n",
        "    else:\n",
        "        await message.channel.send(f\"Wrong! The correct answer was: \\n{correct_answer}\")\n",
        "    # delete user responses once session is over\n",
        "    del user_responses[message.author]\n",
        "\n",
        "\n",
        "# Step 4: Handle new user response\n",
        "async def handle_new_response(message: Message, user_message: str) -> None:\n",
        "    # get response from user\n",
        "    response, answer = get_response(user_message)\n",
        "    await message.channel.send(response)\n",
        "    # if there exists a user response, add it to user_responses to track sessions\n",
        "    if answer:\n",
        "        user_responses[message.author] = {'answer': answer}\n",
        "\n",
        "\n",
        "# Step 5: Handle the startup of the bot\n",
        "@client.event\n",
        "async def on_ready() -> None:\n",
        "    print(f'{client.user} is now running!')\n",
        "\n",
        "\n",
        "# Step 6: Let's handle the messages\n",
        "@client.event\n",
        "async def on_message(message: Message) -> None:\n",
        "    if message.author == client.user:\n",
        "        return\n",
        "\n",
        "    username: str = str(message.author)\n",
        "    user_message: str = message.content\n",
        "    channel: str = str(message.channel)\n",
        "\n",
        "    print(f'[{channel}] {username}: \"{user_message}\"')\n",
        "    await send_message(message, user_message)\n",
        "\n",
        "\n",
        "# Step 7: Main Starting point\n",
        "def main() -> None:\n",
        "    client.run(Token)\n",
        "\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ]
    }
  ]
}