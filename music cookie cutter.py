
class music_der_epoch:
    
    num_of_epochs = 0
        
    def __init__(self, start_event_time, event_duration, event_type):
        
        self.start_event_time = start_event_time
        self.event_duration = event_duration
        self.event_type = event_type
        self.end_event_time = start_event_time + event_duration
        music_der_epoch.num_of_epochs += 1
        
    def after(self, wave_event_time):
        if wave_event_time < self.start_event_time:
            
            print ('FAIL - YOU WERE AFTER')
            
    def metronome(self, BPM, beat_start, beat_end):
        self.BPM = BPM
        self.beat_start = beat_start
        self.beat_end = beat_end
        self.beat_duration = beat_start - beat_end
        
        self.tick_list = []
        tick = float(self.beat_start)
        self.tick_list.append(tick)
        while tick < self.beat_end:
            tick = round((BPM / 60) + tick, 3)
            self.tick_list.append(tick)

        return self.tick_list
            


# epochs
motzart = music_der_epoch(3070.09, 600.99,'Motzart.K448')

dua_lipa_slow = music_der_epoch(320.29, 60.9, 'tempo_slow')
dua_lipa_slow.metronome(77.25, dua_lipa_slow.start_event_time, dua_lipa_slow.end_event_time)

dua_lipa_normal = music_der_epoch(771.1, 60.95, 'tempo_normal')
dua_lipa_normal.metronome(103, dua_lipa_normal.start_event_time, dua_lipa_slow.end_event_time)

dua_lipa_fast = music_der_epoch(1166.05, 61, 'tempo_quick')
dua_lipa_fast.metronome(128.75, dua_lipa_fast.start_event_time, dua_lipa_fast.end_event_time)

low_key_gliding = music_der_epoch(1237.26 , 600.94,'low_key_gliding')
low_key_gliding.metronome(105, low_key_gliding.start_event_time, low_key_gliding.end_event_time)

print(dua_lipa_fast.__dict__)





# epoch_checker