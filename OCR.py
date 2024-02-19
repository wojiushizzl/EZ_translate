from PIL import  ImageGrab,ImageTk
from paddleocr import PaddleOCR, draw_ocr
import numpy as np



# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`

class ZZL_OCR:
    def __init__(self):
        self.en_ocr = PaddleOCR(use_angle_cls=True, lang="en")  # need to run only once to download and load model into memory
        self.ch_ocr = PaddleOCR(use_angle_cls=True,lang="ch")  # need to run only once to download and load model into memory
    def en_OCR(self,img):
        result=self.en_ocr.ocr(img,cls=False)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)
        return result
    def ch_OCR(self,img):
        result=self.ch_ocr.ocr(img,cls=False)
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)
        return result

if __name__ == '__main__':
    bbox = (10,10,500,500)
    screenshot = ImageGrab.grab(bbox=bbox)
    image = np.array(screenshot)
    result = PaddleOCR.ocr(PaddleOCR(),img=image)
    for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(line)
