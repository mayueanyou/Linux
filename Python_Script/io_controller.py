import os,sys


class IO_Controller:
    def __init__(self, port, type):
        self.device = os.open(port, type)
    
    def __del__(self):
        os.close(self.device)
    
    def write(self,data):
        print('write',data)
        os.write(self.device, data)
    
    def read(self,length):
        data = os.read(self.device, length)
        return data
    
    def read_all_in_word(self):
        data_list = []
        while True:
            try:
                data_list.append(self.read(4))
            except:
                break
        return data_list
    
    def write_in_word(self,data):
        data_list = []
        for i in range(int(len(data)/4)):
            data_list.append(data[i*4:(i+1)*4])
        data_list.append(data[(i+1)*4:len(data)])
        if len(data_list[-1]) == 0: data_list.pop(-1)
        else: 
            for i in range(4-len(data_list[-1])):
                data_list[-1] += b' '
        
        for word in data_list:
            self.write(word)
        


if __name__ == '__main__':
    io = IO_Controller('/dev/axis_fifo_0x00000000a0030000', os.O_RDWR)
    #io.write('hell1234'.encode())
    #print(io.read(1024))
    io.write_in_word('1234567890001'.encode())
    print(io.read_all_in_word())
