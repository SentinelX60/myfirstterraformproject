#!/usr/bin/env python3
"""
GCP Infrastructure Diagram Generator
Creates a visual representation of the Terraform-deployed infrastructure
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

def create_gcp_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Remove axes
    ax.axis('off')
    
    # Set background color
    fig.patch.set_facecolor('#f8f9fa')
    
    # Title
    ax.text(5, 7.5, 'GCP Infrastructure - Terraform Deployment', 
            fontsize=20, fontweight='bold', ha='center', 
            color='#1a73e8')
    
    # Subtitle
    ax.text(5, 7.1, 'Free Tier Google Compute Engine VM', 
            fontsize=14, ha='center', color='#5f6368')
    
    # GCP Cloud boundary
    cloud_box = FancyBboxPatch((0.5, 1), 9, 5.5,
                               boxstyle="round,pad=0.1",
                               facecolor='#e8f0fe',
                               edgecolor='#1a73e8',
                               linewidth=2,
                               linestyle='--')
    ax.add_patch(cloud_box)
    
    # GCP Cloud label
    ax.text(1, 6.2, 'Google Cloud Platform', 
            fontsize=12, fontweight='bold', color='#1a73e8')
    
    # Project box
    project_box = FancyBboxPatch((1, 4.5), 8, 1.8,
                                 boxstyle="round,pad=0.05",
                                 facecolor='#fff',
                                 edgecolor='#dadce0',
                                 linewidth=1)
    ax.add_patch(project_box)
    
    # Project info
    ax.text(1.3, 6, 'Project: myfirstterraformproject-xxxxxx', 
            fontsize=11, fontweight='bold', color='#202124')
    ax.text(1.3, 5.7, 'Region: us-central1', 
            fontsize=10, color='#5f6368')
    ax.text(1.3, 5.4, 'Zone: us-central1-a', 
            fontsize=10, color='#5f6368')
    
    # VPC Network box
    vpc_box = FancyBboxPatch((1.5, 2.5), 7, 1.8,
                             boxstyle="round,pad=0.05",
                             facecolor='#f1f8ff',
                             edgecolor='#4285f4',
                             linewidth=1.5)
    ax.add_patch(vpc_box)
    
    # VPC Network label
    ax.text(2, 4, 'Default VPC Network', 
            fontsize=11, fontweight='bold', color='#4285f4')
    
    # Subnet representation
    subnet_box = FancyBboxPatch((2, 2.8), 6, 0.8,
                                boxstyle="round,pad=0.03",
                                facecolor='#e3f2fd',
                                edgecolor='#2196f3',
                                linewidth=1)
    ax.add_patch(subnet_box)
    
    ax.text(2.2, 3.1, 'Default Subnet (us-central1)', 
            fontsize=10, color='#1976d2')
    
    # VM Instance box
    vm_box = FancyBboxPatch((3.5, 1.3), 3, 1.2,
                            boxstyle="round,pad=0.05",
                            facecolor='#fff',
                            edgecolor='#34a853',
                            linewidth=2)
    ax.add_patch(vm_box)
    
    # VM Icon (simplified server representation)
    vm_icon = patches.Rectangle((3.7, 1.8), 0.6, 0.4, 
                               facecolor='#34a853', 
                               edgecolor='#137333')
    ax.add_patch(vm_icon)
    
    # VM details
    ax.text(4.5, 2.1, 'free-tier-vm', 
            fontsize=11, fontweight='bold', color='#137333')
    ax.text(4.5, 1.9, 'Machine Type: f1-micro', 
            fontsize=9, color='#5f6368')
    ax.text(4.5, 1.7, 'OS: Debian 11', 
            fontsize=9, color='#5f6368')
    ax.text(4.5, 1.5, 'Disk: 10GB Boot Disk', 
            fontsize=9, color='#5f6368')
    
    # External IP representation
    external_ip_circle = Circle((7.5, 2), 0.3, 
                               facecolor='#ff9800', 
                               edgecolor='#f57c00')
    ax.add_patch(external_ip_circle)
    
    ax.text(7.5, 2, 'IP', ha='center', va='center', 
            fontsize=8, fontweight='bold', color='white')
    ax.text(7.5, 1.5, 'External IP\n(Ephemeral)', 
            fontsize=9, ha='center', color='#f57c00')
    
    # Internet cloud
    internet_circle = Circle((8.5, 0.5), 0.4, 
                            facecolor='#9e9e9e', 
                            edgecolor='#757575')
    ax.add_patch(internet_circle)
    
    ax.text(8.5, 0.5, 'Internet', ha='center', va='center', 
            fontsize=8, fontweight='bold', color='white')
    
    # Connection lines
    # VM to External IP
    ax.plot([6.5, 7.2], [2, 2], 'k-', linewidth=2, alpha=0.7)
    
    # External IP to Internet
    ax.plot([7.8, 8.1], [1.8, 0.8], 'k-', linewidth=2, alpha=0.7)
    
    # Terraform logo area
    terraform_box = FancyBboxPatch((0.5, 0.1), 2.5, 0.7,
                                   boxstyle="round,pad=0.05",
                                   facecolor='#623ce4',
                                   edgecolor='#623ce4')
    ax.add_patch(terraform_box)
    
    ax.text(1.75, 0.45, 'Terraform', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')
    ax.text(1.75, 0.25, 'Infrastructure as Code', ha='center', va='center',
            fontsize=8, color='white')
    
    # Arrow from Terraform to GCP
    ax.annotate('', xy=(4, 1.3), xytext=(2.5, 0.6),
                arrowprops=dict(arrowstyle='->', lw=2, color='#623ce4'))
    
    # Cost indicator
    cost_box = FancyBboxPatch((7.5, 0.1), 2, 0.7,
                              boxstyle="round,pad=0.05",
                              facecolor='#0f9d58',
                              edgecolor='#0f9d58')
    ax.add_patch(cost_box)
    
    ax.text(8.5, 0.55, 'FREE TIER', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')
    ax.text(8.5, 0.35, '$0/month*', ha='center', va='center',
            fontsize=9, color='white')
    ax.text(8.5, 0.2, '(*within limits)', ha='center', va='center',
            fontsize=7, color='white')
    
    # Legend
    legend_y = 0.3
    ax.text(4.5, legend_y, 'Key Components:', fontsize=10, fontweight='bold')
    
    # Legend items
    legend_items = [
        ('🟦', 'GCP Project & VPC Network'),
        ('🟩', 'Compute Engine VM Instance'), 
        ('🟠', 'External IP Address'),
        ('🟣', 'Terraform Management')
    ]
    
    for i, (icon, desc) in enumerate(legend_items):
        x_pos = 4.5 + (i % 2) * 2.5
        y_pos = 0.1 if i >= 2 else 0.2
        ax.text(x_pos, y_pos, f'{icon} {desc}', fontsize=8)
    
    # Save the diagram
    plt.tight_layout()
    plt.savefig('C:/Users/bryan/Documents/MyFirstTerraformProject/diagram.png', 
                dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
    plt.savefig('C:/Users/bryan/Documents/MyFirstTerraformProject/diagram.pdf', 
                bbox_inches='tight', facecolor='#f8f9fa')
    
    print("✅ Diagram created successfully!")
    print("📁 Files saved:")
    print("   - diagram.png (high-resolution)")
    print("   - diagram.pdf (vector format)")
    
    return fig

if __name__ == "__main__":
    create_gcp_diagram()
    plt.show()
