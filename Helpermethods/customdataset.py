import torch

#classification/regression problems
class CustomDataset:
    def __init__(self, data, targets, tokenizer):
        self.data = data
        self.targets = targets
        self.tokenizer = tokenizer
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        text = self.data[idx]
        
        #if self.target.shape[1] > 1:
        #    target = self.targets[idx, :]
        #else:
        #    target = self.targets[idx]
        
        input_ids = tokenizer(text)
        #take care of padding.

        return {
            "text" : torch.tensor(input_ids, dtype=torch.long),
            #"attention_mask" : if your tokenizer is returning it
            "target" : torch.tensor(target, dtype=torch.long),

        }