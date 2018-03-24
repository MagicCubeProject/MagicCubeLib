import os
from rcube.MagicCube import MCubeState
from rcube.MagicCubeFlags import MCubeSide

class McubeHTMLView(object):
    def __init__(self, magic_cube_state):
        self.mc_state = magic_cube_state
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.template_path = os.path.join(
            file_path,
            "templates/MCubeTemplate.html"
        )

    def set_template(self,path_to_template):
        self.template_path=path_to_template

    def read_template(self):
        with open(self.template_path, "r") as f:
            self.template= f.read()
        f.close()

    def get_state_values(self):
        pass

if __name__ == "__main__":
    mc = MCubeState()
    v = McubeHTMLView(mc)
    print(v.template_path)
