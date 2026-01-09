from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import StringProperty

class grid(GridLayout) :
    content = StringProperty("0")
    def char_insert(self, char) :
        if char=="CLOSE" : 
            exit()
        elif char=="=" :
            try: 
                self.content = str(eval(self.content))
            except ZeroDivisionError: 
                self.content = "0"
        elif char=="CE" : 
            self.content = "0"
        elif char=="C" :
            if char!="0": self.content = self.content[:-1] 
        else : 
            if self.content=="0" :
                self.content = char
            else : 
                self.content += char
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class calculatorApp(App): 
    def build(self) : 
        return grid()
    
calculatorApp().run()