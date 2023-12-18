import torch
import torch.nn as nn

class PositionalEncoding(nn.Module):
    def __init__(self, input_size, max_length):
        super(PositionalEncoding, self).__init__()
        
        self.input_size = input_size
        self.max_length = max_length
        
        self.positional_encoding = self._generate_positional_encoding()
        
    def _generate_positional_encoding(self):
        position = torch.arange(0, self.max_length).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, self.input_size, 2) * -(math.log(10000.0) / self.input_size))
        scaled_time = position * div_term

        # Compute sine and cosine components
        sin_component = torch.sin(scaled_time)
        cos_component = torch.cos(scaled_time)

        # Interleave sine and cosine components
        position_encoding = torch.zeros(self.max_length, self.input_size)
        position_encoding[:, 0::2] = sin_component
        position_encoding[:, 1::2] = cos_component

        return position_encoding.unsqueeze(0)
    
    def forward(self, input):
        batch_size, seq_len, _ = input.size()
        
        # Add positional encoding to the input
        output = input + self.positional_encoding[:, :seq_len, :]
        
        return output