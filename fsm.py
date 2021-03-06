from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text == "go to state1"

    def is_going_to_show_fsm(self, event):
        text = event.message.text
        return text == "fsm"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_show_fsm(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_image_message(reply_token, 'https://https://line-bot-f74089046.herokuapp.com/show-fsm')
        self.go_back()

    def on_exit_show_fsm(self):
        print("Leaving state2")
