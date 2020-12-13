#!/bin/bash

# Script to compute raw results (before post-processing)

CKPT_FILE='/data2/puppala/projects/dynamic_obj/unsupervised_detection/weights/unsupervised_detection_models/davis_best_model/model.best'
DATASET_FILE='/data2/puppala/projects/dynamic_obj/tum/rgbd_dataset_freiburg3_walking_rpy/rgb_new'
#'/data2/puppala/projects/dynamic_obj/kitti/dataset/sequences/05/image_3'
PWC_CKPT_FILE='/data2/puppala/projects/dynamic_obj/unsupervised_detection/weights/pwcnet-lg-6-2-multisteps-chairsthingsmix/pwcnet.ckpt-595000'

python3 test_generator.py \
--dataset=DAVIS2016 \
--ckpt_file=$CKPT_FILE \
--flow_ckpt=$PWC_CKPT_FILE \
--test_crop=0.9 \
--test_temporal_shift=1 \
--root_dir=$DATASET_FILE \
--generate_visualization=True \
--test_save_dir=results/tum_overlayed
