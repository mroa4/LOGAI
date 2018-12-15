import os

class Data:
    def __init__(self,batch_size):
        self.x = []
        self.y = []
        self.x_t = []
        self.y_t = []
        self.i_t = 0
        self.i = 0
        self.batch_size = batch_size
        self.read_all()
        self.n = len(self.x)
        print("N: ", self.n)
    def read_all(self):
        os.chdir("../logs/features/")
        log_files = os.listdir()
        n = len(log_files)
        for i in range(n):
            log_file_name = log_files[i]
            log_file = open(log_file_name, "r")
            log = log_file.read()
            lines = log.split("\n")
            for line in lines:
                if line.find("pt") != -1:
                    continue
                if line == '':
                    continue
                datas = line.split("|")
                x = []
                for i in range(2,len(datas)-2):
                    data = datas[i].split(" ")
                    for d in data:
                        x.append(float(d))
                data = datas[-2].split(" ")
                # y = [float(data[0]), float(data[1])]
                y = onekey(int(data[0])-1,11)
                self.x.append(x)
                self.y.append(y)
        n = len(self.x)
        nn = int(n/10*8)
        self.x_t = self.x[nn:]
        self.y_t = self.y[nn:]
        self.x = self.x[:nn]
        self.y = self.y[:nn]
    def get_batch(self):
        i = self.i
        self.i += self.batch_size
        return self.x[i:i+self.batch_size], self.y[i:i+self.batch_size]
    def get_batch_t(self):
        i = self.i_t
        self.i_t += self.batch_size
        return self.x_t[i:i+self.batch_size], self.y_t[i:i+self.batch_size]

    def restart(self):
        self.i = 0
        self.i_t = 0
def onekey(n,l):
    lst = [0 for i in range(l)]
    lst[n] = 1
    return lst
