import google.generativeai as genai
import os
import pickle
genai.configure(api_key='your-key',transport='rest')
model = genai.GenerativeModel('gemini-pro')
model2 = genai.GenerativeModel('gemini-pro')
model_img = genai.GenerativeModel('gemini-pro-vision')
history = []
chat = model.start_chat(history=history)
while True:
    if os.path.exists('D://123/history.pkl'):
        with open('D://123/history.pkl', 'rb') as f:
            chat.history = pickle.load(f)
    else:
        with open('D://123/history.pkl', 'wb') as f:
            pickle.dump(chat.history, f)
    input_a = input("请输入请求")
    response = chat.send_message(input_a)
    print(response.text)
    print('*'*100)
    print(chat.history)
    print('*' * 100)
    with open('D://123/history.pkl', 'wb') as f:
        pickle.dump(chat.history, f)