C = type("Class", (), {'A': 555,
						'__init__': lambda self, val: setattr(self, "A", val),
						'__str__': lambda self: f"<{self.A}>"})
