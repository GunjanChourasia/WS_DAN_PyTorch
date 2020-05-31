

python train_bap.py test\
    --model-name inception \
    --batch-size 12 \
    --dataset custom \
    --image-size 512 \
    --input-size 448 \
    --checkpoint-path checkpoint/custom/model_best.pth.tar \
    --use-gpu \
    --multi-gpu \
    --gpu-ids 0,1 \
