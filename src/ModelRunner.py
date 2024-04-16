from main import MyPaddleOCR

ocr = MyPaddleOCR()

# 사용 가능한 언어, 모델 조회
# ocr.get_available_langs()
# ocr.get_available_models()

#### 이미지 인식 처리
# 테스트 이미지
# image_path = '../res/test.png'

# 그린한식뷔페 메뉴
# image_path = '../res/menu-20240415.png'

# 더존 메뉴
image_path = '../res/thezone-20240416.png'
result = ocr.run_ocr(img_path=image_path, debug=True)

print("result ", result)
# result = ocr.run_ocr(img_path=, debug=True)