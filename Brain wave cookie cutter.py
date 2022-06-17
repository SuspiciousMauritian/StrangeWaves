
class eeg:
    
    
    def __init__(self, id, file_name, start_second, duration):
        
        self.id = id
        self.file_name = file_name 
        self.start_second = start_second
        self.duration = duration
        
        
        
        # func ICA = 19 componts
        
        # ica 0 = ma ma = cross
        
        # if ma cross list + bmp signifcat
        