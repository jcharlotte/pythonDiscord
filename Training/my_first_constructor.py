class Pony:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
        

    def start(self):
        self.started = True
        self.speed = 5
        print("Ony started walking, let's go!")

    def speed_change(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Pataclop, pataclop !")
            if self.speed == 0:
                self.started = False
        else:
            print("The pony has to start walking first")
    
    def stop(self):
        self.speed = 0
        self.started = False

flutterShy = Pony()

flutterShy.start()
flutterShy.speed_change(40)
print("FlutterShy's speed:", flutterShy.speed)
print("Is FlutterShy moving?", flutterShy.started)
flutterShy.speed_change(-45)
print("FlutterShy's speed:", flutterShy.speed)
print("Is FlutterShy moving?", flutterShy.started)
flutterShy.stop()