# Author: Tomas Hodan (hodantom@cmp.felk.cvut.cz)
# Center for Machine Perception, Czech Technical University in Prague

"""Configuration of the BOP Toolkit."""

import os


######## Basic ########

# Folder with the BOP datasets.
if 'BOP_PATH' in os.environ:
  datasets_path = os.environ['BOP_PATH']
else:
  # datasets_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/data_object_pose'
  datasets_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/data_object_pose'

# Folder with pose results to be evaluated.
# results_path = r'$CAMOZZI_DIR_PATH/zebra_pose/ZebraPose/zebrapose/report/pose_result_bop'
results_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/report/pose_result_bop'

# Folder for the calculated pose errors and performance scores.
# eval_path = r'$CAMOZZI_DIR_PATH/zebra_pose/ZebraPose/zebrapose/report/pose_result_bop/evaluation' 
eval_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/report/pose_result_bop/evaluation' 

######## Extended ########

# Folder for outputs (e.g. visualizations).
# output_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/data_object_pose/lmo/'
output_path = r'$CAMOZZI_DIR_PATH/zebra_pose/data/report/output/'

# For offscreen C++ rendering: Path to the build folder of bop_renderer (github.com/thodan/bop_renderer).
bop_renderer_path = r'$CAMOZZI_DIR_PATH/zebra_pose/ZebraPose/bop_toolkit/bop_renderer'

# Executable of the MeshLab server.
meshlab_server_path = r'/path/to/meshlabserver.exe'
