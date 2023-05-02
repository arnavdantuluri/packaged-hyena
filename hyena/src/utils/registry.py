optimizer = {
    "adam": "torch.optim.Adam",
    "adamw": "torch.optim.AdamW",
    "rmsprop": "torch.optim.RMSprop",
    "sgd": "torch.optim.SGD",
    "lamb": "safari.src.utils.optim.lamb.JITLamb",
}

scheduler = {
    "constant": "transformers.get_constant_schedule",
    "plateau": "torch.optim.lr_scheduler.ReduceLROnPlateau",
    "step": "torch.optim.lr_scheduler.StepLR",
    "multistep": "torch.optim.lr_scheduler.MultiStepLR",
    "cosine": "torch.optim.lr_scheduler.CosineAnnealingLR",
    "constant_warmup": "transformers.get_constant_schedule_with_warmup",
    "linear_warmup": "transformers.get_linear_schedule_with_warmup",
    "cosine_warmup": "transformers.get_cosine_schedule_with_warmup",
    "cosine_warmup_timm": "safari.src.utils.optim.schedulers.TimmCosineLRScheduler",
}

model = {
    # Backbones from this repo
    "model": "safari.src.models.sequence.SequenceModel",
    "lm": "safari.src.models.sequence.long_conv_lm.ConvLMHeadModel",
    "lm_simple": "safari.src.models.sequence.simple_lm.SimpleLMHeadModel",
    "vit_b_16": "safari.src.models.baselines.vit_all.vit_base_patch16_224",
}

layer = {
    "id": "safari.src.models.sequence.base.SequenceIdentity",
    "ff": "safari.src.models.sequence.ff.FF",
    "mha": "safari.src.models.sequence.mha.MultiheadAttention",
    "s4d": "safari.src.models.sequence.ssm.s4d.S4D",
    "s4_simple": "safari.src.models.sequence.ssm.s4_simple.SimpleS4Wrapper",
    "long-conv": "safari.src.models.sequence.long_conv.LongConv",
    "h3": "safari.src.models.sequence.h3.H3",
    "h3-conv": "safari.src.models.sequence.h3_conv.H3Conv",
    "hyena": "safari.src.models.sequence.hyena.HyenaOperator",
    "hyena-filter": "safari.src.models.sequence.hyena.HyenaFilter",
    "vit": "safari.src.models.sequence.mha.VitAttention",
}

callbacks = {
    "timer": "safari.src.callbacks.timer.Timer",
    "params": "safari.src.callbacks.params.ParamsLog",
    "learning_rate_monitor": "pytorch_lightning.callbacks.LearningRateMonitor",
    "model_checkpoint": "pytorch_lightning.callbacks.ModelCheckpoint",
    "early_stopping": "pytorch_lightning.callbacks.EarlyStopping",
    "swa": "pytorch_lightning.callbacks.StochasticWeightAveraging",
    "rich_model_summary": "pytorch_lightning.callbacks.RichModelSummary",
    "rich_progress_bar": "pytorch_lightning.callbacks.RichProgressBar",
    "progressive_resizing": "safari.src.callbacks.progressive_resizing.ProgressiveResizing",
}
