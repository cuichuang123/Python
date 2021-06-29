import uuid

from Hypnos.Hypnos_reply import *
bizUniqueId  = str(uuid.uuid4())


if __name__ == '__main__':
    res = Hypnos_Reply()
    res.Run_reply()

