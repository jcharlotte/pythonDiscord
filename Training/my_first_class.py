class Horse:
    speed = 0
    walking = False

    def start(self):
        self.started = True
        print("Horse started walking, let's go!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Pataclop, pataclop !')
        else:
            print("The horse needs to start moving first")
        
    def stop(self):
        self.speed = 0
        print('The horse stopped walking')


spirit = Horse()
# spirit.increase_speed(10)
spirit.start()
spirit.increase_speed(40)
