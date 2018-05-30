import sys

import numpy as np
import nibabel as nib

# Configuration

initial_size_x = 448
initial_size_y = 448
initial_size_z = 128

pooling_kernel_x = 2
pooling_kernel_y = 2
pooling_kernel_z = 2

new_size_x = int(initial_size_x/pooling_kernel_x)
new_size_y = int(initial_size_y/pooling_kernel_y)
new_size_z = int(initial_size_z/pooling_kernel_z)

initial_data = nib.load(sys.argv[1]+".nii").get_data()
new_data_max = np.zeros((new_size_x,new_size_y,new_size_z),dtype=initial_data.dtype)
#new_data_min = np.zeros((new_size_x,new_size_y,new_size_z),dtype=initial_data.dtype)
#new_data_average = np.zeros((new_size_x,new_size_y,new_size_z),dtype=initial_data.dtype)

for x in range(0,new_size_x):
    for y in range(0,new_size_y):
        for z in range(0,new_size_z):
            ix = int(x * pooling_kernel_x)
            iy = int(y * pooling_kernel_y)
            iz = int(z * pooling_kernel_z)

            pool = initial_data[ix:ix+pooling_kernel_x,iy:iy+pooling_kernel_y,iz:iz+pooling_kernel_z]

            # max
            new_data_max[x, y, z] = pool.max()
            # min
            #new_data_min[x, y, z] = pool.min()
            # average
            #new_data_average[x, y, z] = np.average(pool)

    print((x/new_size_x)*100,'%')
print(100,'%')


img = nib.Nifti1Image(new_data_max, np.eye(4))
img.to_filename(sys.argv[1]+"_max"+".nii")
#img = nib.Nifti1Image(new_data_min, np.eye(4))
#img.to_filename(sys.argv[1]+"_min"+".nii")
#img = nib.Nifti1Image(new_data_average, np.eye(4))
#img.to_filename(sys.argv[1]+"_avg"+".nii")
