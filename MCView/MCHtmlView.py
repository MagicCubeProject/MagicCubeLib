import os

from jinja2 import Environment, FileSystemLoader

from MCState.MCSide.MCElementDirection import MCubeDirection
from MCState.MCState import MagicCubeState
from MCState.MCubeSide import MCubeSide


class MCHtmlView(object):
    """
    "HTML viewer" render Rubik's Cube state to HTML file
    """
    def __init__(self,magic_cube_state=None):
        if magic_cube_state is None:
            self.mc_state = MagicCubeState()
        else:
            self.mc_state = magic_cube_state
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.template_path = os.path.join(
            file_path,
            "templates/MCubeTemplate.html"
        )

    def set_template(self,path_to_template):
        """
        Change default Template to custom.
        For templating used Jinja2.
        :param path_to_template: Path to custom template
        :return:
        """
        self.template_path=path_to_template

    def __read_template(self):
        """
        Reading template content from predefined file path
        :return:
        """
        with open(self.template_path, "r") as f:
            self.template= f.read()
        f.close()

    def __map_state_to_dict(self):
        """

        :return:
        """
        value = dict()
        value["UP_NORTH_WEST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.NORTH_WEST])
        value["UP_NORTH"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.NORTH])
        value["UP_NORTH_EAST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.NORTH_EAST])
        value["UP_WEST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.WEST])
        value["UP_CENTER"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.CENTER])
        value["UP_EAST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.EAST])
        value["UP_SOUTH_WEST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.SOUTH_WEST])
        value["UP_SOUTH"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.SOUTH])
        value["UP_SOUTH_EAST"]= str(self.mc_state[MCubeSide.UP][MCubeDirection.SOUTH_EAST])

        value["FRONT_NORTH_WEST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.NORTH_WEST])
        value["FRONT_NORTH"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.NORTH])
        value["FRONT_NORTH_EAST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.NORTH_EAST])
        value["FRONT_WEST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.WEST])
        value["FRONT_CENTER"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.CENTER])
        value["FRONT_EAST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.EAST])
        value["FRONT_SOUTH_WEST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.SOUTH_WEST])
        value["FRONT_SOUTH"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.SOUTH])
        value["FRONT_SOUTH_EAST"]= str(self.mc_state[MCubeSide.FRONT][MCubeDirection.SOUTH_EAST])

        value["RIGHT_NORTH_WEST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.NORTH_WEST])
        value["RIGHT_NORTH"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.NORTH])
        value["RIGHT_NORTH_EAST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.NORTH_EAST])
        value["RIGHT_WEST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.WEST])
        value["RIGHT_CENTER"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.CENTER])
        value["RIGHT_EAST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.EAST])
        value["RIGHT_SOUTH_WEST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.SOUTH_WEST])
        value["RIGHT_SOUTH"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.SOUTH])
        value["RIGHT_SOUTH_EAST"]= str(self.mc_state[MCubeSide.RIGHT][MCubeDirection.SOUTH_EAST])

        value["LEFT_NORTH_WEST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.NORTH_WEST])
        value["LEFT_NORTH"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.NORTH])
        value["LEFT_NORTH_EAST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.NORTH_EAST])
        value["LEFT_WEST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.WEST])
        value["LEFT_CENTER"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.CENTER])
        value["LEFT_EAST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.EAST])
        value["LEFT_SOUTH_WEST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.SOUTH_WEST])
        value["LEFT_SOUTH"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.SOUTH])
        value["LEFT_SOUTH_EAST"]= str(self.mc_state[MCubeSide.LEFT][MCubeDirection.SOUTH_EAST])

        value["BACK_NORTH_WEST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.NORTH_WEST])
        value["BACK_NORTH"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.NORTH])
        value["BACK_NORTH_EAST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.NORTH_EAST])
        value["BACK_WEST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.WEST])
        value["BACK_CENTER"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.CENTER])
        value["BACK_EAST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.EAST])
        value["BACK_SOUTH_WEST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.SOUTH_WEST])
        value["BACK_SOUTH"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.SOUTH])
        value["BACK_SOUTH_EAST"]= str(self.mc_state[MCubeSide.BACK][MCubeDirection.SOUTH_EAST])

        value["DOWN_NORTH_WEST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.NORTH_WEST])
        value["DOWN_NORTH"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.NORTH])
        value["DOWN_NORTH_EAST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.NORTH_EAST])
        value["DOWN_WEST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.WEST])
        value["DOWN_CENTER"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.CENTER])
        value["DOWN_EAST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.EAST])
        value["DOWN_SOUTH_WEST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.SOUTH_WEST])
        value["DOWN_SOUTH"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.SOUTH])
        value["DOWN_SOUTH_EAST"]= str(self.mc_state[MCubeSide.DOWN][MCubeDirection.SOUTH_EAST])

        return value

    def render(self,save_to_file = True,file_path = None):
        obj_id = id(self.mc_state)
        state_dict = self.__map_state_to_dict()
        j2_env = Environment(loader=FileSystemLoader("/"),trim_blocks=True)
        result = j2_env.get_template(self.template_path).render(values=state_dict,id=obj_id)
        if save_to_file:
            if file_path is None:
                self.file_path =os.path.join('/tmp',"MCState"+str(obj_id)+".html")
            else:
                self.file_path = file_path
            with open(self.file_path, "w+") as f:
                f.write(result)
                f.close()
            return self.file_path
        else:
            return result




