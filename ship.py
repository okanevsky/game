import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        super (Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('images\ship.bmp')#Загрузка изображения выполняется вызовом pygame.image.load(). Функция возвращает поверхность, представляющую корабль; 
        #полученный объект сохраняется в self.image.
        self.rect = self.image.get_rect()#метод get_rect() используется для получения атрибута rect поверхности
        self.screen_rect = screen.get_rect()#сохраняем прямоугольник экрана в self.screen_rect 
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx#присваиваем self.rect.centerx (координата x центра корабля) значение атрибута centerx прямоугольника экрана
        self.rect.bottom = self.screen_rect.bottom#(координата y низа корабля) присваивается значение атрибута bottom прямоугольника экрана. Pygame использует эти 
        #атрибуты rect для позиционирования изображения, чтобы корабль былвыровнен по центру, а его нижний край совпадал с нижним краем экрана.
        self.center = float(self.rect.centerx)#атрибут для хранения более точной позиции корабля
        self.y = float(self.rect.centery)
        # Флаги перемещения
        self.moving_right = False#флаг перемещения корабля вправо
        self.moving_left = False#флаг перемещения корабля влево

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx
    
    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        if self.moving_right and self.rect.right < self.screen_rect.right:#флаг перемещения корабля вправо
            self.center += self.ai_settings.ship_speed_factor#увеличение позиции корабля
        if self.moving_left and self.rect.left > 0:#флаг перемещения корабля влево
            self.center -= self.ai_settings.ship_speed_factor#уменьшение позиции корабля
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center
    

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)