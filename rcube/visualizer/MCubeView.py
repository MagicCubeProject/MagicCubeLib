import os
from jinja2 import Environment, FileSystemLoader
from rcube.MagicCube import MCubeState
from rcube.MagicCubeFlags import MCubeMoves
from rcube.MagicCubeFlags import MCubeSide
from rcube.MagicCubeFlags import MCubeDirection

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
        value = dict()
        value["UP_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.NORTH_WEST))
        value["UP_NORTH"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.NORTH))
        value["UP_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.NORTH_EAST))
        value["UP_WEST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.WEST))
        value["UP_CENTER"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.CENTER))
        value["UP_EAST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.EAST))
        value["UP_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.SOUTH_WEST))
        value["UP_SOUTH"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.SOUTH))
        value["UP_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.UP).get_value(MCubeDirection.SOUTH_EAST))

        value["FRONT_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.NORTH_WEST))
        value["FRONT_NORTH"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.NORTH))
        value["FRONT_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.NORTH_EAST))
        value["FRONT_WEST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.WEST))
        value["FRONT_CENTER"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.CENTER))
        value["FRONT_EAST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.EAST))
        value["FRONT_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.SOUTH_WEST))
        value["FRONT_SOUTH"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.SOUTH))
        value["FRONT_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.FRONT).get_value(MCubeDirection.SOUTH_EAST))

        value["RIGHT_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.NORTH_WEST))
        value["RIGHT_NORTH"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.NORTH))
        value["RIGHT_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.NORTH_EAST))
        value["RIGHT_WEST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.WEST))
        value["RIGHT_CENTER"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.CENTER))
        value["RIGHT_EAST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.EAST))
        value["RIGHT_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.SOUTH_WEST))
        value["RIGHT_SOUTH"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.SOUTH))
        value["RIGHT_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.RIGHT).get_value(MCubeDirection.SOUTH_EAST))

        value["LEFT_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.NORTH_WEST))
        value["LEFT_NORTH"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.NORTH))
        value["LEFT_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.NORTH_EAST))
        value["LEFT_WEST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.WEST))
        value["LEFT_CENTER"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.CENTER))
        value["LEFT_EAST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.EAST))
        value["LEFT_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.SOUTH_WEST))
        value["LEFT_SOUTH"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.SOUTH))
        value["LEFT_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.LEFT).get_value(MCubeDirection.SOUTH_EAST))

        value["BACK_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.NORTH_WEST))
        value["BACK_NORTH"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.NORTH))
        value["BACK_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.NORTH_EAST))
        value["BACK_WEST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.WEST))
        value["BACK_CENTER"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.CENTER))
        value["BACK_EAST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.EAST))
        value["BACK_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.SOUTH_WEST))
        value["BACK_SOUTH"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.SOUTH))
        value["BACK_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.BACK).get_value(MCubeDirection.SOUTH_EAST))

        value["DOWN_NORTH_WEST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.NORTH_WEST))
        value["DOWN_NORTH"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.NORTH))
        value["DOWN_NORTH_EAST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.NORTH_EAST))
        value["DOWN_WEST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.WEST))
        value["DOWN_CENTER"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.CENTER))
        value["DOWN_EAST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.EAST))
        value["DOWN_SOUTH_WEST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.SOUTH_WEST))
        value["DOWN_SOUTH"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.SOUTH))
        value["DOWN_SOUTH_EAST"]= str(self.mc_state.get_side(MCubeSide.DOWN).get_value(MCubeDirection.SOUTH_EAST))

        return value

    def get_html(self):
        obj_id = id(self.mc_state)
        values  = self.get_state_values()
        j2_env = Environment(loader=FileSystemLoader("/"),trim_blocks=True)
        result = j2_env.get_template(self.template_path).render(values=values,id=obj_id)
        with open("./temp"+str(obj_id)+".html", "w+") as f:
                    f.write(result)
                    f.close()

if __name__ == "__main__":
    mc_state = MCubeState()
    print(mc_state)
    nmc = mc_state.get_rotated_state(MCubeSide.FRONT)
    del mc_state
    print(nmc)
    nmc1 =  nmc.get_rotated_state(MCubeSide.UP)
    del nmc
    nmc2 = nmc1.get_rotated_state(MCubeSide.DOWN)
    v = McubeHTMLView(nmc2)
    v.read_template()
    v.get_html()
