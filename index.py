import mido,time,random

i = 0
outport = mido.open_output('Virtual-MIDI-Driver Cable')
inport =  mido.open_input() 
n = 0
def main():
    global i
    n = random.randint(36,40)
    outport.send(mido.Message('note_on', note=n, velocity=5,time=0))
    i += 1

while i <= 105:
    main()
    outport.send(mido.Message('note_off',note=n,velocity=0))
    time.sleep(1)


