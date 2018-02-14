"""
A container for the pipeline
of analysis
"""
from Sample import Sample

class Packet(object):

    def __init__(self):
        self.sample_set = []
        self.result_set = []

    def add_sample(self, s):
        """
            @param: s: a Sample to store in the list
        """
        self.sample_set.append(s)

    def add_result(self, r):
        """
            @param: r: a  result to store in the list
        """
        self.result_set.append(r)

"""
sample1 = Sample()
packet = Packet()

packet.add_sample(sample1)
packet.sample_set[0].emg[1] = "foo"
print(packet.sample_set[0].emg[1])
"""