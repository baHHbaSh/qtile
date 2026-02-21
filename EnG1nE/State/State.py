# ~/.config/qtile/EnG1nE/Sequencer/Seq.py
from libqtile.widget import image, base
import os

class State(image.Image):
    orientations = base.ORIENTATION_BOTH

    def __init__(self, Path:str, Hz:int, cb = lambda x:x, **conf):
        self._Hz = Hz
        self.CurrentFrameInd = 0

        self.cb = cb
        
        # Отладка: проверяем существование директории
        if not os.path.isdir(Path):
            raise FileNotFoundError(f"Directory not found: {Path}")
        
        # Фильтруем только изображения + сортируем
        self._Frames = sorted([
            os.path.join(Path, f) for f in os.listdir(Path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
        ], key=lambda x: (len(x), x.lower()))
        
        # Отладка: проверяем наличие кадров
        if not self._Frames:
            raise ValueError(f"No image files found in: {Path}")
        
        print(f"[Sequence] Loaded {len(self._Frames)} frames from {Path}")
        print(f"[Sequence] First frame: {self._Frames[0]}")
        
        super().__init__(filename=self._Frames[0], **conf)
        self._Timer = None

    def _configure(self, qtile, bar):
        """Вызывается после создания виджета, когда self.qtile уже доступен"""
        super()._configure(qtile, bar)
        self._CreateTimer()

    def _CreateTimer(self, *_):
        if self._Timer:
            self._Timer.cancel()
            self._Timer = None

        interval = 1.0 / min(max(.1, self._Hz), 60)
        self._Timer = self.timeout_add(interval, self._Iter)

    def _Iter(self):
        self.CurrentFrameInd = (self.CurrentFrameInd + 1) % len(self._Frames)
        self.filename = self._Frames[self.CurrentFrameInd]
        
        self.cb(self._Hz)

        self._update_image()
        self.draw()
        
        self._CreateTimer()
        return False  # однократный вызов (таймер уже пересоздан)

    @property
    def Hz(self):
        return self._Hz
    
    @Hz.setter
    def FPS(self, value):
        if value <= 0:
            return
        self._Hz = min(value, 60)
        if self._Timer:  # перезапускаем таймер только если он уже существует
            self._CreateTimer()

    @property
    def MaxFrame(self):
        return len(self._Frames)

    def SetFrame(self, index:int):
        self.filename = self._Frames[index]

    def SetFramePercent(self, Num0to1:float):
        Num0to1 = 0 if Num0to1 < 0 else 1 if Num0to1 > 1 else Num0to1
        self.SetFrame(
            round(Num0to1 * self.MaxFrame)
        )