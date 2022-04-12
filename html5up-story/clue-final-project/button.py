import pygame


class Button:
    def __init__(self, x, y, sx, sy, fill, hover_fill, font, font_size, font_color, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.fill = fill
        self.hover_fill = hover_fill
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.text = text
        self.current = False
        self.button_font = pygame.font.SysFont(font, font_size)

    def show_button(self, display):
        if self.current:
            pygame.draw.rect(display, self.hover_fill, (self.x, self.y, self.sx, self.sy))
        else:
            pygame.draw.rect(display, self.fill, (self.x, self.y, self.sx, self.sy))

        text_surface = self.button_font.render(self.text, False, self.font_color)
        display.blit(text_surface, ((self.x + (self.sx/2) - (self.font_size/2) * (len(self.text)/2) + 10,
                                     (self.y + (self.sy/2) - (self.font_size/2) + 10))))

    def mouse_check(self, mouse_pos, mouse_click):
        if (mouse_pos[0] >= self.x and mouse_pos[0] <= (self.x + self.sx) and mouse_pos[1] >= self.y and mouse_pos[1]<= (self.y + self.sy)):
            self.current = True
            return mouse_click[0]
        else:
            self.current = False
            return False

    def change_xy(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

    # Allows color to be changed for notes
    def set_color(self, fill):
        self.fill = fill

    def get_color(self):
        return self.fill
