from game import Game
import time


if __name__ == "__main__":
    game = Game()
    time.sleep(0.5)  # To let objects initialize
    import cProfile
    
    cProfile.run("game.main()", r"cProfiler\output.dat")

    import pstats
    from pstats import SortKey

    with open(r"cProfiler\output_time.txt", "w") as f:
        p = pstats.Stats(r"cProfiler\output.dat", stream=f)
        p.sort_stats("time").print_stats()

    with open(r"cProfiler\output_calls.txt", "w") as f:
        p = pstats.Stats(r"cProfiler\output.dat", stream=f)
        p.sort_stats("calls").print_stats()