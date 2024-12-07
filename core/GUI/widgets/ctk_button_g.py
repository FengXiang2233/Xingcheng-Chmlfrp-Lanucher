import customtkinter as ctk
import tkinter

from core.GUI.widgets.draw_engine_g import DrawEngineG
from typing import Union, Tuple, Callable, Optional, Any,Literal
from typing_extensions import TypeAlias

class CTkButtonG(ctk.CTkButton):

    noCornerMode: TypeAlias = Literal["top","bottom","left","right"]

    # Override
    def __init__(self,
                 master: Any,
                 width: int = 140,
                 height: int = 28,
                 corner_radius: Optional[int] = None,
                 border_width: Optional[int] = None,
                 border_spacing: int = 2,

                 bg_color: Union[str, Tuple[str, str]] = "transparent",
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                 border_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,

                 background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None,
                 round_width_to_even_numbers: bool = True,
                 round_height_to_even_numbers: bool = True,

                 text: str = "CTkButton",
                 font: Optional[Union[tuple, ctk.CTkFont]] = None,
                 textvariable: Union[tkinter.Variable, None] = None,
                 image: Union[ctk.CTkImage, "ImageTk.PhotoImage", None] = None,
                 state: str = "normal",
                 hover: bool = True,
                 command: Union[Callable[[], Any], None] = None,
                 compound: str = "left",
                 anchor: str = "center",
                 noCorner:noCornerMode=None,
                 **kwargs):

        # transfer basic functionality (bg_color, size, appearance_mode, scaling) to CTkBaseClass
        super().__init__(master=master, bg_color=bg_color, width=width, height=height, **kwargs)

        # shape
        self._corner_radius: int = ctk.ThemeManager.theme["CTkButton"]["corner_radius"] if corner_radius is None else corner_radius
        self._corner_radius = min(self._corner_radius, round(self._current_height / 2))
        self._border_width: int = ctk.ThemeManager.theme["CTkButton"]["border_width"] if border_width is None else border_width
        self._border_spacing: int = border_spacing

        # color
        self._fg_color: Union[str, Tuple[str, str]] = ctk.ThemeManager.theme["CTkButton"]["fg_color"] if fg_color is None else self._check_color_type(fg_color, transparency=True)
        self._hover_color: Union[str, Tuple[str, str]] = ctk.ThemeManager.theme["CTkButton"]["hover_color"] if hover_color is None else self._check_color_type(hover_color)
        self._border_color: Union[str, Tuple[str, str]] = ctk.ThemeManager.theme["CTkButton"]["border_color"] if border_color is None else self._check_color_type(border_color)
        self._text_color: Union[str, Tuple[str, str]] = ctk.ThemeManager.theme["CTkButton"]["text_color"] if text_color is None else self._check_color_type(text_color)
        self._text_color_disabled: Union[str, Tuple[str, str]] = ctk.ThemeManager.theme["CTkButton"]["text_color_disabled"] if text_color_disabled is None else self._check_color_type(text_color_disabled)

        # rendering options
        self._background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = background_corner_colors  # rendering options for DrawEngine
        self._round_width_to_even_numbers: bool = round_width_to_even_numbers  # rendering options for DrawEngine
        self._round_height_to_even_numbers: bool = round_height_to_even_numbers  # rendering options for DrawEngine

        # text, font
        self._text = text
        self._text_label: Union[tkinter.Label, None] = None
        self._textvariable: tkinter.Variable = textvariable
        self._font: Union[tuple, ctk.CTkFont] = ctk.CTkFont() if font is None else self._check_font_type(font)
        if isinstance(self._font, ctk.CTkFont):
            self._font.add_size_configure_callback(self._update_font)

        # image
        self._image = self._check_image_type(image)
        self._image_label: Union[tkinter.Label, None] = None
        if isinstance(self._image, ctk.CTkImage):
            self._image.add_configure_callback(self._update_image)

        # other
        self._state: str = state
        self._hover: bool = hover
        self._command: Callable = command
        self._compound: str = compound
        self._anchor: str = anchor
        self._click_animation_running: bool = False

        # canvas and draw engine
        self._canvas = ctk.CTkCanvas(master=self,
                                 highlightthickness=0,
                                 width=self._apply_widget_scaling(self._desired_width),
                                 height=self._apply_widget_scaling(self._desired_height))
        self._canvas.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="nsew")
        self._draw_engine = DrawEngineG(canvas=self._canvas,noCorner=noCorner)
        self._draw_engine.set_round_to_even_numbers(self._round_width_to_even_numbers, self._round_height_to_even_numbers)  # rendering options

        # configure cursor and initial draw
        self._create_bindings()
        self._set_cursor()
        self._draw()
    # Override
    def _create_grid(self):
        self.grid_propagate(0)
        super()._create_grid()