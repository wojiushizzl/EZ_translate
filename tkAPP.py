import tkinter as tk
from PIL import  ImageGrab,ImageTk


import numpy as np

class FullscreenWindow:
    def __init__(self,ocr,translate,en2zh=1):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.wait_visibility()
        self.root.wm_attributes('-alpha', 0.8)  # 设置窗口透明度，值在0.0（完全透明）到1.0（完全不透明）之间
        self.root.attributes('-topmost',True)
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(),bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.focus_set()

        self.ocr=ocr
        self.translate=translate
        self.translate_mode=en2zh
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        self.rect_ids = []

        # self.button = tk.Button(self.root, text="绘制矩形", command=self.enable_drawing, bg="white")
        # self.button.pack()
        self.root.bind("<Escape>",self.on_escape)
        self.root.bind("<Double-KeyPress-Z>",self.enable_drawing)

        self.canvas.bind("<B1-Motion>", self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.end_drawing)

    def enable_drawing(self,event):
        self.root.wm_attributes('-alpha', 0.1)  # 设置窗口透明度，值在0.0（完全透明）到1.0（完全不透明）之间

        self.start_x = None
        self.start_y = None
        self.rect_id = None
        print("enable")
    def draw_rectangle(self, event):
        if self.start_x is None:
            self.start_x = event.x
            self.start_y = event.y
        else:
            if self.rect_id:
                self.canvas.delete(self.rect_id)
            self.rect_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, event.x, event.y, outline="black",fill="white"
            )
            self.rect_ids.append(self.rect_id)

    def end_drawing(self, event):
        # print(self.start_x,self.start_y)
        # print(event.x,event.y)
        x1=min(self.start_x,event.x)
        y1=min(self.start_y,event.y)
        x2=max(self.start_x,event.x)
        y2=max(self.start_y,event.y)
        bbox=(x1,y1,x2,y2)
        screenshot=ImageGrab.grab(bbox=bbox)
        image=np.array(screenshot)
        # screenshot.show()
        ocr_result=self.ocr.ocr(image)
        if ocr_result[0]  is not  None:
            # print(len(ocr_result[0]))
            o_text=''
            t_text=''
            for _ocr_i in ocr_result[0]:
                print(_ocr_i[1][0])
                o_text= o_text+_ocr_i[1][0]+'\n'

                if self.translate_mode==1:
                    from_code = "en"
                    to_code = "zh"
                else:
                    from_code = "zh"
                    to_code = "en"
                translate_text=self.translate.translate(_ocr_i[1][0],from_code,to_code)
                t_text= t_text+translate_text+'\n'
            self.canvas.create_text(x1, y2, text=o_text, font=("Purisa", 10), anchor=tk.NW,fill='white')
            self.canvas.create_text(x1, y1, text=t_text, font=("Helvetica", 10, "italic"), anchor=tk.SW,fill='white')
            # self.canvas.create_text(x2, y1, text=text, font=("Arial", 10), anchor=tk.NW,fill='white')
            # self.canvas.create_text(x2, y1, text=text, font=("Purisa", 10), anchor=tk.NW,fill='white')
        else:
            print("No text detection")

        self.start_x = None
        self.start_y = None
        self.rect_id = None
        print("end drawing")

    def on_escape(self, event):
        self.root.destroy()
        print("end all")

    def clear_all(self):
        for rect_id in self.rect_ids:
            self.canvas.delete(rect_id)
        self.rect_ids = []


if __name__ == "__main__":
    app = FullscreenWindow()
    app.root.mainloop()
