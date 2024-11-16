import customtkinter as ctk

class CTkButtonG(ctk.CTkButton):
    # Override
    def _create_grid(self):
        self.grid_propagate(0)
        super()._create_grid()