"""CPU-only resource accounting and a toy next-token sampler. Standard library only."""
from math import prod,exp,log
from random import Random

def tensor_bytes(shape,bits):
    if bits<=0 or any(not isinstance(n,int) or n<0 for n in shape):raise ValueError('Invalid shape or bit width')
    return (prod(shape)*bits+7)//8  # ideal tightly packed storage; excludes metadata/padding

def linear_flops(batch,tokens,input_dim,output_dim):
    return 2*batch*tokens*input_dim*output_dim  # multiply-add counts as two; excludes bias

def kv_bytes(batch,context,layers,kv_heads,head_dim,bits=16):
    return tensor_bytes((2,batch,context,layers,kv_heads,head_dim),bits)

def softmax(logits):
    if not logits:raise ValueError('At least one logit required')
    shifted=[exp(x-max(logits)) for x in logits]
    total=sum(shifted)
    return [x/total for x in shifted]

def sample(probabilities,seed=7):
    if not probabilities or any(p<0 for p in probabilities) or abs(sum(probabilities)-1)>1e-9:raise ValueError('Invalid distribution')
    x=Random(seed).random();total=0
    for i,p in enumerate(probabilities):
        total+=p
        if x<total:return i
    return len(probabilities)-1

if __name__=='__main__':
    vocabulary=['blue','green','clear','<end>']
    logits=[2.0,1.0,0.0,-1.0];p=softmax(logits)
    print('Illustrative logits, not outputs of a trained model:',logits)
    print('Probabilities:',[round(x,6) for x in p])
    print('Greedy token:',vocabulary[max(range(len(p)),key=p.__getitem__)])
    print('Seeded sample:',vocabulary[sample(p)])
    print('Loss when correct token is blue:',round(-log(p[0]),6))
    print('BF16 [1024,4096] tensor bytes:',tensor_bytes((1024,4096),16))
    print('Linear [1,128,256] @ [256,1024] FLOPs:',linear_flops(1,128,256,1024))
    print('KV cache bytes (B=1,T=2048,L=12,Hkv=4,Dh=64,BF16):',kv_bytes(1,2048,12,4,64))
