from pynput import keyboard
from  tkAPP import FullscreenWindow
from paddleocr import PaddleOCR
import argostranslate.translate


class KeyboardListener:
    def __init__(self):
        #初始化OCR
        self.ocr_init=PaddleOCR()
        self.translate_init=argostranslate.translate
        # 创建键盘监听器
        with keyboard.Listener(on_press=self.on_press,on_release=self.on_release) as self.listener:
            self.listener.join()
        # 启动监听器
        self.listener.start()
        # 标记Alt键是否被按下
        self.alt_pressed = False
        # self.app=None
    def on_press(self, key):
        try:
            if key.char == 'z' and self.alt_pressed:
                print("按下 alt+'z' 键")
                self.alt_pressed = False
                app = FullscreenWindow(self.ocr_init,self.translate_init,en2zh=1)
                app.root.mainloop()
            if key.char == 'x' and self.alt_pressed:
                print("按下 alt+'x' 键")
                self.alt_pressed = False
                app = FullscreenWindow(self.ocr_init, self.translate_init,en2zh=2)
                app.root.mainloop()
        except AttributeError:
            # 处理特殊按键的情况
            if key ==keyboard.Key.esc:
                # print("esc")
                pass
            if key==keyboard.Key.alt_l:
                # print("alt")
                self.alt_pressed = True
            # print(key)

    def on_release(self,key):
        if key == keyboard.Key.alt_l:
            self.alt_pressed = False
            print("release alt")

if __name__ == "__main__":
    keyboard_listener = KeyboardListener()
