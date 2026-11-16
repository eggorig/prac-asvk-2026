C = type("Class", (), {'__A': 555,
						'__init__': lambda self, val: setattr(self, "__A", val),
						'__str__': lambda self: f"<{self.A}>"})
