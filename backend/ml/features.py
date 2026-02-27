import numpy as np

def entropy_block(block):
    counts = np.bincount(block, minlength=256)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))

def byte_zero_ratio(block):
    return np.mean(block == 0)

def unique_byte_ratio(block):
    return len(np.unique(block)) / 256.0

def variance(block):
    return np.var(block)