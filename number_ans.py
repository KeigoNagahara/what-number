import numpy
from PIL import Image, ImageEnhance, ImageOps
import pickle

def moji_command(image):
    if not image:
        return '画像を指定してください'
    # 学習済みモデルのロード
    with open('./trained-model.pickle', 'rb') as f:
        clf = pickle.load(f)
    f.close()
    # 前処理
    im = Image.open(image.file)
    # 明暗をはっきりさせる
    im_enhanced = ImageEnhance.Brightness(im).enhance(2)
    # グレースケールに変換
    im_gray = im_enhanced.convert(mode='L')
    # 8ピクセル四方に縮小
    im_8x8 = im_gray.resize((8,8))
    # 明暗を反転
    im_inverted = ImageOps.invert(im_8x8)
    # 2次元のndarrayに変換
    X_im2d = numpy.asarray(im_inverted)
    # 1次元のndarrayに変換
    X_im1d = X_im2d.reshape(1, 64)
    # 0~255の値を0~16に変換
    X_multiplied = X_im1d * (16/255)

    # 予測
    y_pred = clf.predict(X_multiplied)
    y_pred = y_pred[0]
    return 'この数字は「{}」です'.format(y_pred)

def number_ans(image):
    response = ''
    try:
        response = moji_command(image)
        return response
    except Exception as e:
        print('エラー')
        print('* 種類:', type(e))
        print('* 内容:', e)
