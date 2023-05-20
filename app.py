from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class cam(App):
    def build(self):
        '''
        
        :return:
        '''
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800,800)


        button_obj = Button(text = "press")
        button_obj.size_hint(.5,.2)
        button_obj.pos_hint = {'x':25, 'y':.25}
        button_obj(on_press = self.shutter)

        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        return layout
    
    def shutter(self, *args):
        self.camera_obj.export_to_png("./shutter.png")
if __name__ == '__main__':
    cam().run()