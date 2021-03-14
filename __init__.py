from mycroft import MycroftSkill, intent_file_handler


class PiTempCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.temp.pi.intent')
    def handle_check_temp_pi(self, message):
        self.speak_dialog('check.temp.pi')


def create_skill():
    return PiTempCheck()

