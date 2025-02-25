from js import setInterval, clearInterval, Audio
from pyodide.ffi import create_proxy

is_playing = False
count = 0
phases = ["Inhale", "Hold", "Exhale", "Wait"]
timer_id = None
sound_enabled = False

def play_tone():
    if sound_enabled:
        audio = Audio('./assets/tone.mp3')
        audio.play()

def update_display():
    Element('timer').write(4 - (count % 4))
    Element('phase').write(phases[count % 4])

def breathing_cycle():
    global count
    count += 1
    play_tone()
    update_display()

def toggle_play():
    global is_playing, timer_id
    is_playing = not is_playing
    
    if is_playing:
        timer_id = setInterval(create_proxy(breathing_cycle), 4000)
        Element('btnText').write("Pause")
    else:
        clearInterval(timer_id)
        Element('btnText').write("Start")

def toggle_sound():
    global sound_enabled
    sound_enabled = not sound_enabled
