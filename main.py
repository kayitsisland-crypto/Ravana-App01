from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import gps
import requests
import threading

class RavanaApp(App):
    def build(self):
        self.is_running = False
        # සරල UI එකක් බිල්ඩ් එකේ බර අඩු කරන්න
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.label = Label(
            text="RAVANA AGENT\nSTATUS: READY", 
            font_size='24sp', 
            halign='center',
            color=(0, 1, 1, 1)
        )
        
        self.btn = Button(
            text="START MISSION", 
            size_hint=(1, 0.3), 
            background_color=(0, 0.8, 0.4, 1),
            font_size='20sp'
        )
        self.btn.bind(on_release=self.toggle)
        
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        return layout

    def toggle(self, instance):
        if not self.is_running:
            try:
                gps.configure(on_location=self.on_location)
                gps.start(minTime=5000, minDistance=1)
                self.is_running = True
                self.btn.text = "STOP MISSION"
                self.btn.background_color = (0.9, 0.1, 0.1, 1)
                self.label.text = "MISSION ACTIVE\nTRANSMITTING..."
            except Exception as e:
                self.label.text = f"GPS Error:\nCheck Permissions"
        else:
            gps.stop()
            self.is_running = False
            self.btn.text = "START MISSION"
            self.btn.background_color = (0, 0.8, 0.4, 1)
            self.label.text = "MISSION TERMINATED\nSYSTEM READY"

    def on_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        self.label.text = f"LIVE LOCATION\nLAT: {lat:.5f}\nLON: {lon:.5f}"
        # Background thread එකකින් data යවනවා UI එක හිර නොවෙන්න
        threading.Thread(target=self.send_data, args=(lat, lon), daemon=True).start()

    def send_data(self, lat, lon):
        # උඹේ Ngrok URL එක
        url = "https://unfineable-suzie-prodisarmament.ngrok-free.dev/update_location"
        headers = {"ngrok-skip-browser-warning": "1"}
        payload = {
            "uid": "AGENT-001",
            "lat": lat,
            "lon": lon,
            "status": "ACTIVE"
        }
        try:
            requests.post(url, json=payload, headers=headers, timeout=5)
        except:
            pass

if __name__ == "__main__":
    RavanaApp().run()
