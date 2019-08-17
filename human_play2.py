from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from tensorflow.keras.models import load_model

from game import State
from pv_mcts import pv_mcts_action

model = load_model('./model/best.h5')
state = State()
next_action = pv_mcts_action(model, 0.0)


class MyWedget(Widget):

    def reset(self):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 0, .5)
            Line(points=[160, 0, 160, 480], width=2, close='True')
            Line(points=[320, 0, 320, 480], width=2, close='True')
            Line(points=[0, 160, 480, 160], width=2, close='True')
            Line(points=[0, 320, 480, 320], width=2, close='True')

    def on_touch_down(self, touch):
        ''' クリックイベント '''
        self.turn_of_human(touch)

    # 人間のターン
    def turn_of_human(self, touch):
        global state

        # ゲーム終了時
        if state.is_done():
            state = State()
            self.reset()
            return

        # 先手でない時
        if not state.is_first_player():
            return

        # クリック位置を行動に変換
        x = int(touch.pos[0] / 160)
        y = int(touch.pos[1] / 160)
        action = x + y * 3

        if x < 0 or 2 < x or y < 0 or 2 < y:  # 範囲外
            return

        # 合法手でない時
        if not (action in state.legal_actions()):
            return

        # 次の状態の取得
        state = state.next(action)

        # 丸追加
        self.draw_piece(action)

        # AIのターン
        self.turn_of_ai()

    # AIのターン
    def turn_of_ai(self):
        global state

        # ゲーム終了時
        if state.is_done():
            return

        # 行動の取得
        action = next_action(state)

        # 次の状態の取得
        state = state.next(action)

        # バツ追加
        self.draw_piece(action)

    def draw_piece(self, action):
        global state
        x = (action % 3) * 160 + 20
        y = int(action / 3) * 160 + 20
        with self.canvas:
            Color(1, 1, 0, .5)
            if state.is_first_player():
                Line(points=[x, y, x + 120, y + 120], width=3, close='True')
                Line(points=[x + 120, y, x, y + 120], width=3, close='True')
            else:
                Ellipse(pos=(x, y), size=(120, 120))


class IntroKivy(App):
    def build(self):
        Window.size = (240, 240)
        Window.clearcolor = (0, 0.5, 0.5, 1)
        widget = MyWedget()
        widget.reset()
        return widget


if __name__ == "__main__":
    IntroKivy().run()
