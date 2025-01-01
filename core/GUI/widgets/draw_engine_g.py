import customtkinter as ctk
import tkinter
import math
import sys
from typing import Union

class DrawEngineG(ctk.DrawEngine):

    # Override
    def __init__(self,noCorner=None,**kwargs):
        self.noCorner=noCorner
        super().__init__(**kwargs)
    def __calc_optimal_corner_radius(self, user_corner_radius: Union[float, int]) -> Union[float, int]:
        # optimize for drawing with polygon shapes
        if self.preferred_drawing_method == "polygon_shapes":
            if sys.platform == "darwin":
                return user_corner_radius
            else:
                return round(user_corner_radius)

        # optimize for drawing with antialiased font shapes
        elif self.preferred_drawing_method == "font_shapes":
            return round(user_corner_radius)

        # optimize for drawing with circles and rects
        elif self.preferred_drawing_method == "circle_shapes":
            user_corner_radius = 0.5 * round(user_corner_radius / 0.5)  # round to 0.5 steps

            # make sure the value is always with .5 at the end for smoother corners
            if user_corner_radius == 0:
                return 0
            elif user_corner_radius % 1 == 0:
                return user_corner_radius + 0.5
            else:
                return user_corner_radius
    def draw_rounded_rect_with_border(self, width: Union[float, int], height: Union[float, int], corner_radius: Union[float, int],
                                      border_width: Union[float, int], overwrite_preferred_drawing_method: str = None) -> bool:
        """ Draws a rounded rectangle with a corner_radius and border_width on the canvas. The border elements have a 'border_parts' tag,
            the main foreground elements have an 'inner_parts' tag to color the elements accordingly.

            returns bool if recoloring is necessary """

        if self._round_width_to_even_numbers:
            width = math.floor(width / 2) * 2  # round (floor) _current_width and _current_height and restrict them to even values only
        if self._round_height_to_even_numbers:
            height = math.floor(height / 2) * 2
        corner_radius = round(corner_radius)

        if corner_radius > width / 2 or corner_radius > height / 2:  # restrict corner_radius if it's too large
            corner_radius = min(width / 2, height / 2)

        border_width = round(border_width)
        corner_radius = self.__calc_optimal_corner_radius(corner_radius)  # optimize corner_radius for different drawing methods (different rounding)

        if corner_radius >= border_width:
            inner_corner_radius = corner_radius - border_width
        else:
            inner_corner_radius = 0

        if overwrite_preferred_drawing_method is not None:
            preferred_drawing_method = overwrite_preferred_drawing_method
        else:
            preferred_drawing_method = self.preferred_drawing_method

        if preferred_drawing_method == "polygon_shapes":
            return self.__draw_rounded_rect_with_border_polygon_shapes(width, height, corner_radius, border_width, inner_corner_radius)
        elif preferred_drawing_method == "font_shapes":
            return self.__draw_rounded_rect_with_border_font_shapes(width, height, corner_radius, border_width, inner_corner_radius, ())
        elif preferred_drawing_method == "circle_shapes":
            return self.__draw_rounded_rect_with_border_circle_shapes(width, height, corner_radius, border_width, inner_corner_radius)
    # Override
    def __draw_rounded_rect_with_border_font_shapes(self, width: int, height: int, corner_radius: int, border_width: int, inner_corner_radius: int,
                                                    exclude_parts: tuple) -> bool:
        requires_recoloring = False
        # create border button parts
        if border_width > 0:
            if corner_radius > 0:
                # create canvas border corner parts if not already created, but only if needed, and delete if not needed
                if not self._canvas.find_withtag("border_oval_1_a") and "border_oval_1" not in exclude_parts:
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_1_a", "border_corner_part", "border_parts"), anchor=tkinter.CENTER)
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_1_b", "border_corner_part", "border_parts"), anchor=tkinter.CENTER, angle=180)
                    requires_recoloring = True
                elif self._canvas.find_withtag("border_oval_1_a") and "border_oval_1" in exclude_parts:
                    self._canvas.delete("border_oval_1_a", "border_oval_1_b")

                if not self._canvas.find_withtag("border_oval_2_a") and width > 2 * corner_radius and "border_oval_2" not in exclude_parts:
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_2_a", "border_corner_part", "border_parts"), anchor=tkinter.CENTER)
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_2_b", "border_corner_part", "border_parts"), anchor=tkinter.CENTER, angle=180)
                    requires_recoloring = True
                elif self._canvas.find_withtag("border_oval_2_a") and (not width > 2 * corner_radius or "border_oval_2" in exclude_parts):
                    self._canvas.delete("border_oval_2_a", "border_oval_2_b")

                if not self._canvas.find_withtag("border_oval_3_a") and height > 2 * corner_radius \
                    and width > 2 * corner_radius and "border_oval_3" not in exclude_parts:
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_3_a", "border_corner_part", "border_parts"), anchor=tkinter.CENTER)
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_3_b", "border_corner_part", "border_parts"), anchor=tkinter.CENTER, angle=180)
                    requires_recoloring = True
                elif self._canvas.find_withtag("border_oval_3_a") and (not (height > 2 * corner_radius
                                                                            and width > 2 * corner_radius) or "border_oval_3" in exclude_parts):
                    self._canvas.delete("border_oval_3_a", "border_oval_3_b")

                if not self._canvas.find_withtag("border_oval_4_a") and height > 2 * corner_radius and "border_oval_4" not in exclude_parts:
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_4_a", "border_corner_part", "border_parts"), anchor=tkinter.CENTER)
                    self._canvas.create_aa_circle(0, 0, 0, tags=("border_oval_4_b", "border_corner_part", "border_parts"), anchor=tkinter.CENTER, angle=180)
                    requires_recoloring = True
                elif self._canvas.find_withtag("border_oval_4_a") and (not height > 2 * corner_radius or "border_oval_4" in exclude_parts):
                    self._canvas.delete("border_oval_4_a", "border_oval_4_b")

                # change position of border corner parts
                self._canvas.coords("border_oval_1_a", corner_radius, corner_radius, corner_radius)
                self._canvas.coords("border_oval_1_b", corner_radius, corner_radius, corner_radius)
                self._canvas.coords("border_oval_2_a", width - corner_radius, corner_radius, corner_radius)
                self._canvas.coords("border_oval_2_b", width - corner_radius, corner_radius, corner_radius)
                self._canvas.coords("border_oval_3_a", width - corner_radius, height - corner_radius, corner_radius)
                self._canvas.coords("border_oval_3_b", width - corner_radius, height - corner_radius, corner_radius)
                self._canvas.coords("border_oval_4_a", corner_radius, height - corner_radius, corner_radius)
                self._canvas.coords("border_oval_4_b", corner_radius, height - corner_radius, corner_radius)

            else:
                self._canvas.delete("border_corner_part")  # delete border corner parts if not needed

            # create canvas border rectangle parts if not already created
            if not self._canvas.find_withtag("border_rectangle_1"):
                self._canvas.create_rectangle(0, 0, 0, 0, tags=("border_rectangle_1", "border_rectangle_part", "border_parts"), width=0)
                self._canvas.create_rectangle(0, 0, 0, 0, tags=("border_rectangle_2", "border_rectangle_part", "border_parts"), width=0)
                requires_recoloring = True

            # change position of border rectangle parts
            self._canvas.coords("border_rectangle_1", (0, corner_radius, width, height - corner_radius))
            self._canvas.coords("border_rectangle_2", (corner_radius, 0, width - corner_radius, height))

        else:
            self._canvas.delete("border_parts")

        # create inner button parts
        if inner_corner_radius > 0:

            # create canvas border corner parts if not already created, but only if they're needed and delete if not needed
            if not self._canvas.find_withtag("inner_oval_1_a") and "inner_oval_1" not in exclude_parts:
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_1_a", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER)
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_1_b", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER, angle=180)
                requires_recoloring = True
            elif self._canvas.find_withtag("inner_oval_1_a") and "inner_oval_1" in exclude_parts:
                self._canvas.delete("inner_oval_1_a", "inner_oval_1_b")

            if not self._canvas.find_withtag("inner_oval_2_a") and width - (2 * border_width) > 2 * inner_corner_radius and "inner_oval_2" not in exclude_parts:
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_2_a", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER)
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_2_b", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER, angle=180)
                requires_recoloring = True
            elif self._canvas.find_withtag("inner_oval_2_a") and (not width - (2 * border_width) > 2 * inner_corner_radius or "inner_oval_2" in exclude_parts):
                self._canvas.delete("inner_oval_2_a", "inner_oval_2_b")

            if not self._canvas.find_withtag("inner_oval_3_a") and height - (2 * border_width) > 2 * inner_corner_radius \
                and width - (2 * border_width) > 2 * inner_corner_radius and "inner_oval_3" not in exclude_parts:
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_3_a", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER)
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_3_b", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER, angle=180)
                requires_recoloring = True
            elif self._canvas.find_withtag("inner_oval_3_a") and (not (height - (2 * border_width) > 2 * inner_corner_radius
                                                                       and width - (2 * border_width) > 2 * inner_corner_radius) or "inner_oval_3" in exclude_parts):
                self._canvas.delete("inner_oval_3_a", "inner_oval_3_b")

            if not self._canvas.find_withtag("inner_oval_4_a") and height - (2 * border_width) > 2 * inner_corner_radius and "inner_oval_4" not in exclude_parts:
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_4_a", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER)
                self._canvas.create_aa_circle(0, 0, 0, tags=("inner_oval_4_b", "inner_corner_part", "inner_parts"), anchor=tkinter.CENTER, angle=180)
                requires_recoloring = True
            elif self._canvas.find_withtag("inner_oval_4_a") and (not height - (2 * border_width) > 2 * inner_corner_radius or "inner_oval_4" in exclude_parts):
                self._canvas.delete("inner_oval_4_a", "inner_oval_4_b")

            # change position of border corner parts
            self._canvas.coords("inner_oval_1_a", border_width + inner_corner_radius, border_width + inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_1_b", border_width + inner_corner_radius, border_width + inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_2_a", width - border_width - inner_corner_radius, border_width + inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_2_b", width - border_width - inner_corner_radius, border_width + inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_3_a", width - border_width - inner_corner_radius, height - border_width - inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_3_b", width - border_width - inner_corner_radius, height - border_width - inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_4_a", border_width + inner_corner_radius, height - border_width - inner_corner_radius, inner_corner_radius)
            self._canvas.coords("inner_oval_4_b", border_width + inner_corner_radius, height - border_width - inner_corner_radius, inner_corner_radius)
        else:
            self._canvas.delete("inner_corner_part")  # delete inner corner parts if not needed

        # create canvas inner rectangle parts if not already created
        if not self._canvas.find_withtag("inner_rectangle_1"):
            self._canvas.create_rectangle(0, 0, 0, 0, tags=("inner_rectangle_1", "inner_rectangle_part", "inner_parts"), width=0)
            requires_recoloring = True

        if not self._canvas.find_withtag("inner_rectangle_2") and inner_corner_radius * 2 < height - (border_width * 2):
            self._canvas.create_rectangle(0, 0, 0, 0, tags=("inner_rectangle_2", "inner_rectangle_part", "inner_parts"), width=0)
            requires_recoloring = True

        elif self._canvas.find_withtag("inner_rectangle_2") and not inner_corner_radius * 2 < height - (border_width * 2):
            self._canvas.delete("inner_rectangle_2")
        if self.noCorner == "left":left=0
        else:left=inner_corner_radius
        if self.noCorner == "right":right=0
        else:right=inner_corner_radius
        if self.noCorner == "top":top=0
        else:top=inner_corner_radius
        if self.noCorner == "bottom":bottom=0
        else:bottom=inner_corner_radius
        # change position of inner rectangle parts
        self._canvas.coords("inner_rectangle_1", (border_width + left,
                                                  border_width,
                                                  width - border_width - right,
                                                  height - border_width))
        self._canvas.coords("inner_rectangle_2", (border_width,
                                                  border_width + top,
                                                  width - border_width,
                                                  height - bottom - border_width))

        if requires_recoloring:  # new parts were added -> manage z-order
            self._canvas.tag_lower("inner_parts")
            self._canvas.tag_lower("border_parts")
            self._canvas.tag_lower("background_parts")

        return requires_recoloring