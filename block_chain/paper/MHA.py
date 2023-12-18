import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, input_size, hidden_size, num_heads):
        super(MultiHeadAttention, self).__init__()
        
        self.num_heads = num_heads
        self.hidden_size = hidden_size
        self.head_size = hidden_size // num_heads
        
        self.query_linear = nn.Linear(input_size, hidden_size)
        self.key_linear = nn.Linear(input_size, hidden_size)
        self.value_linear = nn.Linear(input_size, hidden_size)
        self.output_linear = nn.Linear(hidden_size, hidden_size)
        
    def forward(self, input):
        batch_size, seq_len, _ = input.size()
        
        # Linearly transform inputs to query, key, and value
        query = self.query_linear(input)
        key = self.key_linear(input)
        value = self.value_linear(input)
        
        # Reshape query, key, and value
        query = query.view(batch_size, seq_len, self.num_heads, self.head_size).transpose(1, 2)
        key = key.view(batch_size, seq_len, self.num_heads, self.head_size).transpose(1, 2)
        value = value.view(batch_size, seq_len, self.num_heads, self.head_size).transpose(1, 2)
        
        # Compute scaled dot-product attention
        scores = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.head_size, dtype=torch.float32))
        attention_weights = torch.softmax(scores, dim=-1)
        attention_output = torch.matmul(attention_weights, value)
        
        # Reshape and concatenate attention heads
        attention_output = attention_output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.hidden_size)
        
        # Linearly transform attention output
        output = self.output_linear(attention_output)
        
        return output