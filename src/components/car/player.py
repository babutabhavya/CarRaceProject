from src.base.car import AbstractCar
from src.constants.images import RED_CAR_IMAGE


class PlayerCar(AbstractCar):
    IMG = RED_CAR_IMAGE
    START_POS = (180, 200)

    def reduce_speed(self) -> None:
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self) -> None:
        self.vel = -self.vel
        self.move()
