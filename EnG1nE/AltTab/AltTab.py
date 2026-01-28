from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import hook

class AltTab:
    def __init__(self, keys: list):
        # История как переменная экземпляра (НЕ классовая!)
        self.history = ["1", "2"]
        
        # Автоматически обновляем историю при ЛЮБОМ переключении группы
        hook.subscribe.setgroup(self._update_history)
        
        # Добавляем Alt+Tab в переданный список клавиш
        keys.append(
            Key(["mod1"], "Tab", lazy.function(self.alt_tab), desc="Alt+Tab между группами")
        )
    
    def _update_history(self):
        """Добавляем текущую группу в историю при любом переключении"""
        from libqtile import qtile
        current = qtile.current_group.name
        if self.history[-1] != current:
            self.history.append(current)
            if len(self.history) > 2:
                self.history.pop(0)
    
    def alt_tab(self, qtile):
        """Переключение по Alt+Tab: меняем местами последние две группы"""
        if len(self.history) >= 2:
            # Меняем местами последние две записи
            self.history[-1], self.history[-2] = self.history[-2], self.history[-1]
            target = self.history[-1]
            if target in qtile.groups_map:
                qtile.groups_map[target].toscreen()