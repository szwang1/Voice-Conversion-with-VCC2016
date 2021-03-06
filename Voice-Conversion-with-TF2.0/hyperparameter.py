class Hyperparameter:
    logdir = 'logdir'
    weights_dir = 'weights'
    data_dir = 'datasets'
    rate = 22050
    batch_size = 1
    generator_lr = 0.0002
    discriminator_lr = 0.0001
    lambda_cycle = 10
    lambda_identity = 5
    num_mceps = 36
    duration = 5.0
    n_frames = 128
    output_size = 512
    num_iterations = 4000#200000

    # data augmentation.
    n_mask_frames = 8
