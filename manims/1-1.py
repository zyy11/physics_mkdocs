from manim import *

class Translation(Scene):
    def construct(self):
        t = ValueTracker(0)
        def get_ori(t):
            t = t.get_value() - 1
            return 4 * t * RIGHT + t * (t + 1) * (t - 1) * UP * 5

        triangle = always_redraw(lambda: Polygon(LEFT, DOWN*2, UP + RIGHT).shift(get_ori(t)).set_fill(BLUE, opacity=0.8))

        dots = VGroup(always_redraw(lambda: Dot(triangle.get_vertices()[0])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[1])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[2])))
        for dot in dots:
           self.add(TracedPath(dot.get_center))

        self.add(triangle, dots)
        self.play(t.animate.set_value(2), rate_func=linear, run_time=4)
        self.wait(1)

class Rotation(Scene):
    def construct(self):
        t = ValueTracker(0)
        triangle = always_redraw(lambda: Polygon(LEFT, DOWN*2, UP + RIGHT).rotate(t.get_value()*PI,about_point=ORIGIN).set_fill(BLUE, opacity=0.8))
        dots = VGroup(always_redraw(lambda: Dot(triangle.get_vertices()[0])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[1])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[2])))
        for dot in dots:
            self.add(TracedPath(dot.get_center))

        self.add(triangle, dots)
        self.play(t.animate.set_value(2), rate_func=linear, run_time=4)
        self.wait(1)

class Movement(Scene):
    def construct(self):
        t = ValueTracker(0)

        def get_ori(t):
            t = t.get_value() - 1
            return 4 * t * RIGHT + t * (t + 1) * (t - 1) * UP * 5

        triangle = always_redraw(lambda: Polygon(LEFT, DOWN*2, UP + RIGHT).shift(get_ori(t)).rotate(t.get_value()*PI,about_point=get_ori(t)).set_fill(BLUE, opacity=0.8))

        dots = VGroup(always_redraw(lambda: Dot(triangle.get_vertices()[0])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[1])),
                      always_redraw(lambda: Dot(triangle.get_vertices()[2])))
        for dot in dots:
            self.add(TracedPath(dot.get_center))

        self.add(triangle, dots)
        self.play(t.animate.set_value(2), rate_func=linear, run_time=4)
        self.wait(1)