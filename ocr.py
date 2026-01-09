import cv2
import pytesseract

def ocr_zone(img, x1, y1, x2, y2):
    zone = img[y1:y2, x1:x2]
    gray = cv2.cvtColor(zone, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]
    return pytesseract.image_to_string(gray, lang="fra")

def extract_stats(image_path):
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    left = ocr_zone(img, 0, 0, w//3, h)
    center = ocr_zone(img, w//3, 0, 2*w//3, h)
    right = ocr_zone(img, 2*w//3, 0, w, h)

    return {
        "zones": {
            "left": left,
            "center": center,
            "right": right
        }
    }
