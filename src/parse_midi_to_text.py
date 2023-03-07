import os
import midi
# from midi import *

def parseMidi(filename, part):
  # pattern = midi.read_midifile("./midi/original/debby.midi")
  pattern = midi.read_midifile(filename)
  chunk_str_list = []

  chunk_str = "rs_" + str(pattern.resolution)
  chunk_str_list.append(chunk_str)

  for i, chunk in enumerate(pattern[part]):
    chunk_str = ""

    if (chunk.name == "Note On"):
      chunk_str = chunk_str + str(chunk.tick) + "_" + "no" + "_" + str(chunk.pitch) + \
                    "_" + str(chunk.velocity)

      chunk_str_list.append(chunk_str)

    elif (chunk.name == "Set Tempo"):
      chunk_str = chunk_str + str(chunk.tick) + "_" + "st" + "_" + str(int(chunk.bpm)) + "_" + str(int(chunk.mpqn))
      chunk_str_list.append(chunk_str)

    elif (chunk.name == "Control Change"):
      chunk_str = chunk_str + str(chunk.tick) + "_" + "cc" + "_" + str(chunk.channel)  + "_" + \
                      str(chunk.data[0]) + "_" + str(chunk.data[1])
      chunk_str_list.append(chunk_str)
  return chunk_str_list

def writeOutChunks(filenames):
    if not os.path.exists("./miditext/"):
      os.mkdir("./miditext/")
      os.mkdir("./miditext/original/")
    elif not os.path.exists("./miditext/original/"):
      os.mkdir("./miditext/original/")
    # empty out in case of overwrite
    open('./miditext/original/original-song.txt', 'w').close()
    f = open('./miditext/original/original-song.txt', 'w')
    for file in filenames:
      chunk_str_list = parseMidi(file,0)
      for elm in chunk_str_list:
        f.write(str(elm) + "\n")
    f.close()

# parseMidi("./midi/original/young_revised.mid", 0)
# files = ["./midi/original/bluegreen_Revised.mid", "./midi/original/young_revised.mid"]
files = ["./midi/original/AutumnL_Revised.mid"]

writeOutChunks(files)