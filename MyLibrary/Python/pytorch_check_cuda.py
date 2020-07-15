import torch
print(torch.version.cuda)
print(torch.cuda.is_available())
if(torch.cuda.is_available()):
    print(torch.cuda.get_device_name())
    print(torch.cuda.device_count())
