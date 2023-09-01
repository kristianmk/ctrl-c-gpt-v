# ctrl-c-gpt-v
A Python program for correcting spelling and grammar in clipboard content utilizing GPT-4.

https://github.com/kristianmk/ctrl-c-gpt-v/assets/1713062/6bc7555e-c5cf-41a6-8383-9e9e3ab8fa91


**WARNING: If you press the 'rewrite' button, be informed that all content on your clipboard will be sent to OpenAI through their API.**

## Usage
1. Clone this repository.
2. Add your OpenAI API key to the environment variable OPENAI_API_KEY, or, although not recommended, you can add it directly to App.py.. Currently, access to GPT-4 and API calls requires a subscription to the paid version.
3. Install dependencies (use a virtual environment!) `pip install -r requirements.txt`
4. Run `App.py` with your Python interpreter.
5. Select a portion of text within a browser or an editor, and copy it to your clipboard. Anticipate the appearance of two buttons. By selecting 'Rewrite', the content will be transmitted to OpenAI and the original content on your clipboard will be replaced. You can then paste the improved version.

## In Summary:

`Ctrl+C  -->  GPT-4  -->  Ctrl+V`

(Naturally, utilize the command key in place of Ctrl if you are using MacOS)
