import openai
import tkinter as tk
import threading

openai.api_key = ""

# Set up chat completion parameters, only model_engine in use right now
model_engine = "gpt-3.5-turbo-0301"
max_tokens = 60
temperature = 0.8

class MessageList:
    _msgs = []
    
    def AddNew(self, inRole, inMSG):
        x = {
        "role": inRole,
        "content": inMSG
        }
        self._msgs.append(x)

    def GetList(self):
        return self._msgs

    def ClearMSG(self):
        self._msgs.clear()

def get_messages(input_userlist, input_responselist):
    msgList = MessageList()
    msgList.ClearMSG()
    msgList.AddNew("system", sys_box.get("9.0", "end")) # Only 1 sysmsg
    for i in range(1, len(input_userlist)): # Each user message should have 1 corresponsing assistant response
        # This is lazy
        try:
            msgList.AddNew("user", input_userlist[i])
        except:
            pass
        try:
            msgList.AddNew("assistant", input_responselist[i])
        except:
            pass
    
    return msgList


def get_response():
    # Get input text from the user
    input_text = text_box.get("1.0", "end")
    response_text = output_box.get("1.0", "end")

    input_userlist = input_text.split("user: ") # For each of these the role will be set to user later
    input_responselist = response_text.split("assistant: ") #likewise

    # Generate chat completion
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages = get_messages(input_userlist, input_responselist).GetList(),
        stream=True,
        frequency_penalty=0.23
        )

    # Get completed text from OpenAI API response
    output_box.insert("end", "assistant: ")
    for chunk in response:
        #the first response has ['role'] and it was getting on my nerves
        try:
            output_box.insert("end", chunk['choices'][0]['delta']['content'])
        except:
            pass
        output_box.see("end")
    
    output_box.insert("end", "\n\n")
    text_box.insert("end", "\n\nuser: ")
    text_box.see("end")


root = tk.Tk()

text_box = tk.Text(root, wrap="word")
text_box.pack(fill="x")
text_box.insert("end", "user: ")

send_button = tk.Button(root, text="Send", command=lambda : threading.Thread(target=get_response).start())
send_button.pack(fill="x")

output_box = tk.Text(root, wrap="word")
output_box.pack(fill="x")

sys_box = tk.Text(root, wrap="word")
sys_box.pack(fill="x")
sys_box.insert("end", "system: ")

root.mainloop()
