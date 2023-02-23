from parse_midi_to_text import *
from generate_music import *
from training import *


def main(filename):
    fn = "./midi/original/" + filename + ".mid"
    # parts in the midi file, melody/soprano is defaulted 1
    parseMidi(fn, 1)
    # epoch size, batch size
    training(64, 128)
    for i in range(1,3):
        outFn = filename+str(i)+"epoch64"
        generator(outFn)

main("MyFoolishHeart")