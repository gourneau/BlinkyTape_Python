import time
import sys
from BlinkyTape import BlinkyTape


class ModeManager(object):

    def __init__(self, device='/dev/ttyACM0', *args, **kwargs):
        self.bb = BlinkyTape(device)

    def render(self, colors):
        self.bb.send_list(colors)

    def run_mode(self, mode):
        while True:
            start = time.time()
            mode.calc_next_step()
            self.render(mode.get_colors())
            if not mode.no_sleep:
                renderTime = time.time() - start
                time.sleep(1.0/mode.fps - renderTime)
            diff = time.time() - start
            sys.stdout.write("%.02f fps                    \r" % (1.0/diff))

if __name__ == "__main__":
    mm = ModeManager()
    from IPython import embed
    embed()
