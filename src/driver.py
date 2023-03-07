from parse_midi_to_text import *
from generate_music import *
from training import *


def main(files, epoch, batch):
    # fn = "./midi/original/" + filename + ".mid"
    # parts in the midi file, melody/soprano is defaulted 1
    # parseMidi(fn, 0)
    # epoch size, batch size
    # for i in range(32, 129, 32):
    # parseMidi("./midi/original/young_revised.mid", 0)

    # files = ["./midi/original/bluegreen_Revised.mid"]

    writeOutChunks(files)
    training(epoch, batch)

    # outFn = filename + "_epoch_" + str(epoch)
    outFn = "autumnL+BG" + "_epoch_" + str(epoch) + "_batch_" + str(batch)
    generator(outFn)
    # open('./miditext/original/original-song.txt', 'w').close()


# files = ["./midi/original/bluegreen_Revised.mid", "./midi/original/young_revised.mid"]
files = ["./midi/original/AutumnL_Revised.mid","./midi/original/bluegreen_Revised.mid",]
# main(files, 64, 64)
main(files, 64, 512)
# main(files, 256, 128)