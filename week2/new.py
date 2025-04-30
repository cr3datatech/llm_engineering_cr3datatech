import torch
import torch.nn as nn

class LLM(nn.Module):
    def __init__(self, vocab_size, embed_size, num_layers, num_heads):
        super(LLM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.transformer_layers = nn.TransformerEncoderLayer(embed_size, num_heads)
        self.transformer = nn.TransformerEncoder(self.transformer_layers, num_layers)
        self.fc = nn.Linear(embed_size, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        return self.fc(x)

# Example of instantiation and forward pass
vocab_size = 10000  # hypothetical vocabulary size
embed_size = 256    # size of each embedding
num_layers = 6      # number of transformer layers
num_heads = 8       # number of attention heads

# Create the model
model = LLM(vocab_size, embed_size, num_layers, num_heads)

# Dummy input (e.g., a sequence of token indices)
input_sequence = torch.randint(0, vocab_size, (10, 32))  # (sequence_length, batch_size)

# Forward pass
output = model(input_sequence)