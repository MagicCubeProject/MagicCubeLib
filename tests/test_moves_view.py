from rcube.MagicCube import MCubeState
from rcube.MagicCubeFlags import MCubeMoves
from rcube.visualizer.MCubeView import McubeHTMLView
def main():
    for move in MCubeMoves:
         print(move)
         mymc = MCubeState()
         nmc = mymc.get_the_moved_state([move])
         mcv = McubeHTMLView(nmc)
         mcv.read_template()
         mcv.get_html()
         del mcv

if __name__ == '__main__':
    main()
