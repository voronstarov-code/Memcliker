import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import json
import os
import random

# Генерация 100 этапов
stages = []
base = 100
mult = 1
while len(stages) < 100:
    if len(stages) % 10 == 0 and len(stages) > 0:
        mult *= 2
    stages.append(int(base * mult))
    base += 50

class MemClickerApp(App):
    def build(self):
        self.data_file = "save3.json"
        self.load_data()
        self.root = BoxLayout(orientation='vertical', spacing=3, padding=8)
        self.build_ui()
        Clock.schedule_interval(self.update, 0.5)
        return self.root
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                d = json.load(f)
        else: d = {}
        self.coins = d.get("coins", 0)
        self.emeralds = d.get("emeralds", 0)
        self.click_power = d.get("click_power", 1)
        self.max_energy = d.get("max_energy", 100)
        self.energy = d.get("energy", 100)
        self.regen = d.get("regen", 1)
        self.stage = d.get("stage", 0)
        self.clicks_total = d.get("clicks_total", 0)
        self.auto_active = d.get("auto_active", 0)
        self.boost_click = d.get("boost_click", 0)
        self.boost_energy = d.get("boost_energy", 0)
        self.boost_emerald = d.get("boost_emerald", 0)
        self.boost_gold = d.get("boost_gold", 0)
        self.boost_speed = d.get("boost_speed", 0)
        self.boost_mega = d.get("boost_mega", 0)
        self.boost_turbo = d.get("boost_turbo", 0)
        self.boost_ultra = d.get("boost_ultra", 0)
        self.boost_x10 = d.get("boost_x10", 0)
        self.boost_time = d.get("boost_time", 0)
        self.up_click = d.get("up_click", 1)
        self.up_regen = d.get("up_regen", 1)
        self.up_emerald = d.get("up_emerald", 1)
    
    def save(self):
        d = {
            "coins": self.coins,
            "emeralds": self.emeralds,
            "click_power": self.click_power,
            "max_energy": self.max_energy,
            "energy": self.energy,
            "regen": self.regen,
            "stage": self.stage,
            "clicks_total": self.clicks_total,
            "auto_active": self.auto_active,
            "boost_click": self.boost_click,
            "boost_energy": self.boost_energy,
            "boost_emerald": self.boost_emerald,
            "boost_gold": self.boost_gold,
            "boost_speed": self.boost_speed,
            "boost_mega": self.boost_mega,
            "boost_turbo": self.boost_turbo,
            "boost_ultra": self.boost_ultra,
            "boost_x10": self.boost_x10,
            "boost_time": self.boost_time,
            "up_click": self.up_click,
            "up_regen": self.up_regen,
            "up_emerald": self.up_emerald
        }
        with open(self.data_file, "w") as f:
            json.dump(d, f)
    
    def build_ui(self):
        top = BoxLayout(size_hint=(1, 0.1))
        self.lbl_coins = Label(text=f"💰{int(self.coins)}", font_size=20)
        self.lbl_emeralds = Label(text=f"💎{int(self.emeralds)}", font_size=20)
        self.lbl_stage = Label(text=f"🏁{self.stage+1}/{len(stages)}", font_size=16)
        top.add_widget(self.lbl_coins)
        top.add_widget(self.lbl_emeralds)
        top.add_widget(self.lbl_stage)
        self.root.add_widget(top)
        
        self.energy_bar = ProgressBar(max=self.max_energy, value=self.energy, size_hint=(1, 0.05))
        self.root.add_widget(self.energy_bar)
        self.lbl_energy = Label(text=f"⚡{int(self.energy)}/{self.max_energy}", size_hint=(1, 0.05), font_size=14)
        self.root.add_widget(self.lbl_energy)
        
        self.btn_click = Button(text="🔹 КЛИК", font_size=30, size_hint=(1, 0.2), background_color=(0.2,0.4,0.7,1))
        self.btn_click.bind(on_press=self.on_click)
        self.root.add_widget(self.btn_click)
        
        self.lbl_status = Label(text="", size_hint=(1, 0.05), font_size=14)
        self.root.add_widget(self.lbl_status)
        
        shop_label = Label(text="🛒 МАГАЗИН", size_hint=(1, 0.05), font_size=18)
        self.root.add_widget(shop_label)
        
        scroll = ScrollView(size_hint=(1, 0.4))
        grid = GridLayout(cols=3, spacing=3, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        shop_items = [
            ("+1 клик", 50, "click"),
            ("+реген", 40, "regen"),
            ("💎+1", 60, "emerald_up"),
            ("🔥 х2 клик 10с", 30, "boost_click"),
            ("💧 х2 энергия 10с", 25, "boost_energy"),
            ("💎 х2 изумруды 15с", 40, "boost_emerald"),
            ("💰 монеты х2 20с", 50, "boost_gold"),
            ("⚡ авто-клик 30с", 80, "boost_speed"),
            ("🚀 мега-клик х5 5с", 100, "boost_mega"),
            ("🌀 турбо-реген 10с", 70, "boost_turbo"),
            ("⭐ ультра-буст 8с", 120, "boost_ultra"),
            ("🔱 х10 3с", 200, "boost_x10"),
            ("⏳ время +5с ко всем", 90, "boost_time")
        ]
        for name, price, key in shop_items:
            btn = Button(text=f"{name}\n{price}💎", size_hint_y=None, height=60)
            btn.bind(on_press=lambda x, k=key, p=price: self.buy_boost(k, p))
            grid.add_widget(btn)
        
        scroll.add_widget(grid)
        self.root.add_widget(scroll)
    
    def on_click(self, instance):
        if self.energy >= 1:
            self.energy -= 1
            gain = self.click_power
            if self.boost_click > 0: gain *= 2
            if self.boost_gold > 0: gain *= 2
            if self.boost_mega > 0: gain *= 5
            if self.boost_x10 > 0: gain *= 10
            self.coins += gain
            self.clicks_total += 1
            self.btn_click.text = random.choice(["🔥", "💥", "⚡", "💎", "🚀"]) + " КЛИК"
            
            if self.clicks_total % 100 == 0:
                self.emeralds += 5
                self.lbl_status.text = "💎 +5 изумрудов за 100 кликов!"
            if self.clicks_total % 1000 == 0:
                self.emeralds += 20
                self.lbl_status.text = "💎 +20 изумрудов за 1000 кликов!"
            if self.clicks_total % 10000 == 0:
                self.emeralds += 100
                self.lbl_status.text = "💎 +100 изумрудов за 10к кликов!"
            
            self.update_ui()
            self.save()
    
    def buy_boost(self, key, price):
        if self.emeralds < price:
            self.lbl_status.text = "❌ Не хватает изумрудов"
            return
        self.emeralds -= price
        if key == "click":
            self.up_click += 1
            self.click_power += 1
        elif key == "regen":
            self.up_regen += 1
            self.regen += 1
        elif key == "emerald_up":
            self.up_emerald += 1
            self.emeralds += 10
        elif key == "boost_click":
            self.boost_click = 10
        elif key == "boost_energy":
            self.boost_energy = 10
        elif key == "boost_emerald":
            self.boost_emerald = 15
        elif key == "boost_gold":
            self.boost_gold = 20
        elif key == "boost_speed":
            self.auto_active = 30
        elif key == "boost_mega":
            self.boost_mega = 5
        elif key == "boost_turbo":
            self.boost_turbo = 10
        elif key == "boost_ultra":
            self.boost_ultra = 8
        elif key == "boost_x10":
            self.boost_x10 = 3
        elif key == "boost_time":
            self.boost_time += 5
            for b in ["boost_click","boost_energy","boost_emerald","boost_gold","boost_speed","boost_mega","boost_turbo","boost_ultra","boost_x10"]:
                if getattr(self, b, 0) > 0:
                    setattr(self, b, getattr(self, b) + 5)
        self.lbl_status.text = "✅ Куплено!"
        self.update_ui()
        self.save()
    
    def update(self, dt):
        regen = self.regen
        if self.boost_energy > 0: regen *= 2
        if self.boost_turbo > 0: regen *= 3
        self.energy = min(self.max_energy, self.energy + regen)
        
        if self.auto_active > 0 and self.energy >= 1:
            self.energy -= 1
            gain = self.click_power
            if self.boost_click > 0: gain *= 2
            if self.boost_gold > 0: gain *= 2
            if self.boost_mega > 0: gain *= 5
            if self.boost_x10 > 0: gain *= 10
            self.coins += gain
            self.clicks_total += 1
        
        if self.boost_emerald > 0:
            self.emeralds += 0.5
        
        for b in ["boost_click","boost_energy","boost_emerald","boost_gold","boost_speed","boost_mega","boost_turbo","boost_ultra","boost_x10"]:
            val = getattr(self, b, 0)
            if val > 0:
                setattr(self, b, val - 1)
        
        if self.auto_active > 0:
            self.auto_active -= 1
        
        if self.stage < len(stages)-1 and self.coins >= stages[self.stage]:
            self.stage += 1
            self.emeralds += 50
            self.lbl_status.text = f"🏁 Этап {self.stage+1}! +50💎"
        
        self.update_ui()
        self.save()
    
    def update_ui(self):
        self.lbl_coins.text = f"💰{int(self.coins)}"
        self.lbl_emeralds.text = f"💎{int(self.emeralds)}"
        self.lbl_stage.text = f"🏁{self.stage+1}/{len(stages)}"
        self.lbl_energy.text = f"⚡{int(self.energy)}/{self.max_energy}"
        self.energy_bar.max = self.max_energy
        self.energy_bar.value = self.energy

if __name__ == "__main__":
    MemClickerApp().run()
