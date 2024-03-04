# pylint: disable=
import os
from enum import Enum
from typing import List

import pygame


class Animation:
    FRAME_RATE = 25

    def __init__(self, src: str) -> None:
        self.frames = self.load_images(src)

    def load_images(self, src: str) -> List[str]:
        gif_frames = []
        for lose_filename in sorted(os.listdir(src)):
            lose_frame = pygame.image.load(
                os.path.join(src, lose_filename)
            ).convert_alpha()
            gif_frames.append(lose_frame)
        return gif_frames

    def draw(self, win: pygame.Surface, clock: pygame.time.Clock) -> None:
        frame_index = 0
        counter = 0
        while frame_index <= len(self.frames) and counter == 0:
            if frame_index == len(self.frames) - 1:
                counter += 1
            # Blit the current frame onto the screen
            win.blit(self.frames[frame_index], (75, 250))

            # Update the frame index for the next frame
            frame_index = (frame_index + 1) % len(self.frames)
            pygame.display.flip()
            clock.tick(self.FRAME_RATE)


class AnimationType(Enum):
    WINNING = 1
    LOSE = 2


class AnimationFactory:
    @staticmethod
    def get_animation(animation_type: AnimationType) -> Animation:
        if animation_type == AnimationType.WINNING:
            return Animation("src/assets/images/winning-frames")
        if animation_type == AnimationType.LOSE:
            return Animation("src/assets/images/losing-frames")
        raise Exception("Unknown Animation Type")
