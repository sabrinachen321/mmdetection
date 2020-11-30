from mmdet.apis import init_detector, inference_detector
import mmcv
import time


# Specify the path to model config and checkpoint file
config_file = 'configs/headdataset/gfl_r50_fpn_mstrain_2x_headdataset.py'
checkpoint_file = 'logs/headdataset_gfl_r50_fpn_mstrain_2x/latest.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = 'demo/timg.jpeg'  # or img = mmcv.imread(img), which will only load it once

start = time.time()
result = inference_detector(model, img)
end = time.time()
print(end - start)

# visualize the results in a new window
model.show_result(img, result)
# or save the visualization results to image files
model.show_result(img, result, out_file='demo/result.jpeg')

# test a video and show the results
# video = mmcv.VideoReader('video.mp4')
# for frame in video:
#     result = inference_detector(model, frame)
#     model.show_result(frame, result, wait_time=1)