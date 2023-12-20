# setup
import google.generativeai as genai
import PIL.Image
import google.ai.generativelanguage_v1beta.types.content
from IPython.display import display
from IPython.display import Markdown
genai.configure(api_key='your_key',transport='rest')
model = genai.GenerativeModel('gemini-pro')
model_img = genai.GenerativeModel('gemini-pro-vision')
history = []
chat = model.start_chat(history=history)
def create_part(text, role):
    return {
        'text': text,
        'role': role
    }
def img(str):
    img = PIL.Image.open(str)
    new_size = (200, 200)
    img = img.resize(new_size)
    return img
while True:
    input_arr = []
    input_a = input("请输入请求")
    for i in input_a.split(','):
        input_arr.append(i)
    if len(input_arr) == 1:
        response = chat.send_message(input_arr[0])
        print(response.text)
    if len(input_arr) == 2:
        chat_img = model_img.start_chat()
        response = chat_img.send_message([input_arr[0],img(input_arr[1])])
        response.resolve()
        Markdown(response.text)
        print(response.text)
        responsesss = chat.send_message(f'记住我们说过这段对话，我说：{input_arr[0]},你说：{response.text}')