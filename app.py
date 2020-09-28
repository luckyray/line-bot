from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1FpBKamNROvfxZ1v5q3LL24wH7FV3wvp/EAWfl1w9P6tzduukcs37iKtfJGVhaTHEr0eQpMcDrVN/RFmQ3RpSyn8AIlbJZrIf07w8+SHbM/Enr68t1BC9UmF94XXcxN9ApTqr+0/gDckaQFnWTd4sQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3dabcb733965046566d2a9a84b1fa981')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text,
	s = 'hello world!'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()