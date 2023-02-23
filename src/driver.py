from parse_midi_to_text import *
from generate_music import *
from training import *


def main(filename, epoch, batch):
    fn = "./midi/original/" + filename + ".mid"
    # parts in the midi file, melody/soprano is defaulted 1
    parseMidi(fn, 1)
    # epoch size, batch size
    training(epoch, batch)
    outFn = filename+"epoch" + epoch
    generator(outFn)

main("MyFoolishHeart", 32, 128)