from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random

# Quant 本地AI核心
class QuantAICore:
    def get_market_info(self, code):
        trend = ["上涨", "震荡", "下跌"][random.randint(0,2)]
        score = round(random.uniform(60,95),1)
        return f"标的：{code}\nAI趋势：{trend}\nAI评分：{score}分"

    def ai_strategy_signal(self):
        signals = [
            "AI策略：低风险 观望持仓",
            "AI策略：中度机会 小仓位介入",
            "AI策略：高概率趋势 分批建仓",
            "AI策略：风险偏高 暂时回避"
        ]
        return random.choice(signals)

    def run_backtest(self):
        annual = round(random.uniform(8,18),2)
        drawdown = round(random.uniform(3,8),2)
        win_rate = round(random.uniform(55,72),1)
        return f"年化收益：{annual}%\n最大回撤：{drawdown}%\n胜率：{win_rate}%"

class QuantApp(App):
    def build(self):
        Window.soft_input_mode = "resize"
        self.core = QuantAICore()
        panel = TabbedPanel(do_default_tab=False)

        # 行情页
        tab1 = TabbedPanelItem(text="行情")
        lay1 = BoxLayout(orientation="vertical", padding=15, spacing=12)
        self.code_in = TextInput(hint_text="输入股票/币代码")
        lay1.add_widget(self.code_in)
        btn_q = Button(text="AI行情分析")
        btn_q.bind(on_press=self.query_market)
        lay1.add_widget(btn_q)
        self.lab1 = Label(text="请输入代码")
        lay1.add_widget(self.lab1)
        tab1.add_widget(lay1)
        panel.add_widget(tab1)

        # AI策略页
        tab2 = TabbedPanelItem(text="AI策略")
        lay2 = BoxLayout(orientation="vertical", padding=15)
        btn_ai = Button(text="生成AI交易策略")
        btn_ai.bind(on_press=self.gen_strategy)
        lay2.add_widget(btn_ai)
        self.lab2 = Label(text="点击生成策略")
        lay2.add_widget(self.lab2)
        tab2.add_widget(lay2)
        panel.add_widget(tab2)

        # 回测页
        tab3 = TabbedPanelItem(text="回测")
        lay3 = BoxLayout(orientation="vertical", padding=15)
        btn_bt = Button(text="开始AI回测")
        btn_bt.bind(on_press=self.do_backtest)
        lay3.add_widget(btn_bt)
        self.lab3 = Label(text="等待回测")
        lay3.add_widget(self.lab3)
        tab3.add_widget(lay3)
        panel.add_widget(tab3)

        return panel

    def query_market(self, _):
        code = self.code_in.text.strip()
        self.lab1.text = self.core.get_market_info(code) if code else "请输入标的代码"

    def gen_strategy(self, _):
        self.lab2.text = self.core.ai_strategy_signal()

    def do_backtest(self, _):
        self.lab3.text = self.core.run_backtest()

if __name__ == "__main__":
    QuantApp().run()