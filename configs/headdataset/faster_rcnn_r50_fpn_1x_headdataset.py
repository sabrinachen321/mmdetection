# The new config inherits a base config to highlight the necessary modification
_base_ = '../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
        )
    )
)

# Modify dataset related settings
dataset_type = 'HeadDataset'
data_root = 'data/headdataset/'
data = dict(    
    train=dict(
        type=dataset_type,
        ann_file='trainval.txt',
        data_root=data_root,
        img_prefix='imgs'
    ),
    val=dict(
        type=dataset_type,
        ann_file='test.txt',
        data_root=data_root,
        img_prefix='imgs'
    ),
    test=dict(
        type=dataset_type,
        ann_file='test.txt',
        data_root=data_root,
        img_prefix='imgs'
    )
)

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
work_dir = 'logs/headdataset_faster_rcnn_r50_fpn_1x'
evaluation = dict(interval=3, metric='mAP')