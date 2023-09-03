class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def scale(self, factor: float) -> 'Circle':
        """Return a new Circle instance with the radius scaled by the given factor."""
        return Circle(self.radius * factor)
