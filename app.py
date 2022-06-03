import torch

if __name__=="__main__":
    print("In app")
    cuda_avail = torch.cuda.is_available()
    print(cuda_avail)
