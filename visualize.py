# Helper funciton
import matplotlib.pyplot as plt

def visualize(grid, timestep, save_path):
    plt.figure(figsize=(10,8))
    plt.imhsow(grid.detach().cpu().numpy(), cmap='viridis')
    plt.colorbar()
    plt.title(f'Noise Adjustment Grid at Timestep {timestep}')
    plt.savefig(save_path)
    plt.close()
