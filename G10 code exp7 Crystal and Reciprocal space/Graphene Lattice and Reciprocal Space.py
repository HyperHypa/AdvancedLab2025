import numpy as np
import matplotlib.pyplot as plt

def generate_graphene_lattice(rows, cols, a=1.42):
    """Generate 2D graphene lattice coordinates."""
    a1 = np.array([np.sqrt(3) * a, 0]) # Real space lattice vector 1
    a2 = np.array([np.sqrt(3)/2 * a, 3/2 * a]) # lattice vector 2, vector basis (not basis)
    basis = [np.array([0, 0]), np.array([0, a])] # the smallest group of atoms
    atoms = [] # all the locations of the atoms

    for i in range(rows):
        for j in range(cols):
            R = i * a1 + j * a2
            atoms.append(R) # this appends the locations of the atoms
            # if you want to create the full structure of graphene, append the other atom here
            #atoms.append(R+np.array([0, a])) # this is created using the basis shown above

    return np.array(atoms), a1, a2

def generate_reciprocal_vector(a1, a2):
    # lattice vectors -> reciprocal lattice vectors
    a1 = np.append(a1, 0) # add the z dimension
    a2 = np.append(a2, 0) # add the z dimension
    a3 = np.array([0, 0, 1]) # created a unit vector perpendicular to lattice vectors a1 and a2

    # calculates reciprocal lattice vectors with lattice vectors
    b1 = 2 * np.pi * np.cross(a2, a3) / (a1 @ np.cross(a2, a3))
    b2 = 2 * np.pi * np.cross(a1, a3) / (a2 @ np.cross(a1, a3))
    b3 = 2 * np.pi * np.cross(a1, a2) / (a3 @ np.cross(a1, a2)) # not necessary but should be on the z axis
    return b1, b2, b3

# Parameters
rows = 5 # amount extended right
cols = 5 # amount extended up
a = 1.42 # carbon–carbon bond length
atoms, a1, a2 = generate_graphene_lattice(rows, cols, a)
b1, b2, b3 = generate_reciprocal_vector(a1, a2)

# print the lattice vectors and reciprocal lattice vectors
print("Lattice vectors:", a1, a2)
print("Reciprocal lattice vectors:", b1, b2, b3) # note: b3 is only for checking

# Plot atoms and bonds
plt.figure(figsize=(8, 8)) # set plot size
plt.scatter(atoms[:, 0], atoms[:, 1], c='black', s=10, zorder=3) # set the scatter points
plt.title("Graphene Lattice") # set title
plt.xlabel("x (Å)") # set x label
plt.ylabel("y (Å)") # set y label
plt.gca().set_aspect('equal') # set x an y distance on the graph as 1:1 ratio
plt.grid(True, linestyle='--', alpha=0.3) # set a grid as a visualize helper
plt.show() # show the plot
