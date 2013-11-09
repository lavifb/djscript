import pygame.mixer


# may want different values than defaults
pygame.mixer.init()


class Sound:
	def __init__(filename):
		sound = pygame.mixer.Sound(filename)

	def setloop(self):
		raw_input('')
		start = self.sound.get




def crossfade(outsound, insound, time):
	outsound.sound.fadeout(time)
	insound.sound.play(fade_ms=time)
