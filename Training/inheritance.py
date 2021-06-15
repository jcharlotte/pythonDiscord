class Equine:
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


class Zebra(Equine):
    eat_grass = True
    run_away = False
    def scared(self):
        self.run_away = True
        self.eat_grass = False
    
    def safe(self):
        self.run_away = False
        self.eat_grass = True


wildZebra = Zebra()

print("Zebra's speed:", wildZebra.speed)

class Horse(Equine):
    def __init__(self, started = True, speed = 5):
        self.started = started
        self.speed = speed

class Donkey(Equine):
    def start(self):
        self.started = False
        print("It won't move !")


stubbornDonkey = Donkey()
stubbornDonkey.start()