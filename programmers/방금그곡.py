def solution(m, musicinfos):
    music = dict()
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for info in musicinfos:
        start, end, name, code = info.split(',')
        code = code.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        start_t = list(map(int, start.split(':')))
        end_t = list(map(int, end.split(':')))
        time = (end_t[0] * 60 + end_t[1]) - (start_t[0] * 60 + start_t[1])
        repeat = time // len(code)
        music[name] = (code * (repeat + 1))[:time]

    answer = ''
    music[answer] = '0'
    for name, code in music.items():
        if m in code and len(code) > len(music[answer]):
            answer = name
            
    return '(None)' if answer == '' else answer