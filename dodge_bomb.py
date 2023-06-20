import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
kk_img = pg.image.load("ex02/fig/3.png")
#kk_imgs = [pg.transform.rotozoom(kk_img, 0, 2.0), pg.transform.rotozoom(kk_img, 45, 2.0), pg.transform.rotozoom(kk_img, 90, 2.0), pg.transform.rotozoom(kk_img, 135, 2.0), pg.transform.rotozoom(kk_img, 180, 2.0), pg.transform.rotozoom(kk_img, 225, 2.0), pg.transform.rotozoom(kk_img, 270, 2.0), pg.transform.rotozoom(kk_img, 315, 2.0), pg.transform.rotozoom(kk_img, 360, 2.0)]
kk_imgs4 = pg.transform.flip(kk_img, True, False)
kk_imgs1 = pg.transform.rotozoom(kk_img, -90, 1.0)
kk_imgs3 = pg.transform.flip(kk_imgs1, True, False)
kk_imgs2 = pg.transform.rotozoom(kk_img, -90, 1.0)
kk_imgs7 = pg.transform.rotozoom(kk_img, 45, 1.0)
kk_imgs5 = pg.transform.flip(kk_imgs7, True, False)
kk_imgs6 = pg.transform.rotozoom(kk_imgs2, 180, 1.0)

def init_kk_img():
    return{
    (0, 0):kk_img,
    (-5, 0):kk_img, 
    (-5, -5):kk_imgs1, 
    (0, -5):kk_imgs2, 
    (+5, -5):kk_imgs3, 
    (+5, 0):kk_imgs4, 
    (+5, +5):kk_imgs5, 
    (0, +5):kk_imgs6, 
    (-5, +5):kk_imgs7
    }



def check_bound(rect:pg.rect) -> tuple[bool, bool]:
    """
    こうかとんRect，爆弾Rectが画面外 or 画面内かを判定する関数
    引数：こうかとんRect or 爆弾Rect
    戻り値：横方向，縦方向の判定結果タプル（True：画面内／False：画面外）
    """

    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko, tate



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_imgs = [pg.transform.rotozoom(kk_img, 0, 2.0), pg.transform.rotozoom(kk_img, 45, 2.0), pg.transform.rotozoom(kk_img, 90, 2.0), pg.transform.rotozoom(kk_img, 135, 2.0), pg.transform.rotozoom(kk_img, 180, 2.0), pg.transform.rotozoom(kk_img, 225, 2.0), pg.transform.rotozoom(kk_img, 270, 2.0), pg.transform.rotozoom(kk_img, 315, 2.0), pg.transform.rotozoom(kk_img, 360, 2.0)]
    # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect() # 
    kk_rct.center = 900, 400 # 中心を設定する 

    kk_imgss = init_kk_img() #関数呼び出し
    kk_img = kk_imgss[(0, 0)]

    bd_img = pg.Surface((20, 20)) # 練習1
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    bd_img.set_colorkey((0, 0, 0))
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    # ランダムでx,yを生成する。
    bd_rct = bd_img.get_rect()
    bd_rct.center = x, y # 乱数xとyの中心座標を乱数で生成する
    vx, vy = +5, +5
    #練習2

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bd_rct):  # 練習５
            print("ゲームオーバー")
            return   # ゲームオーバー
            
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        

        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        kk_img = kk_imgss[tuple(sum_mv)]

        screen.blit(bg_img, [0, 0]) # 背景画像
        screen.blit(kk_img, kk_rct)
        
        bd_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rct)
        if not yoko:  # 横方向に画面外だったら
            vx *= -1
        if not tate:  # 縦方向に範囲外だったら
            vy *= -1
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()