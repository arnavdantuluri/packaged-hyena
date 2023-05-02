optimizer = {
    "adam": "torch.optim.Adam",
    "adamw": "torch.optim.AdamW",
    "rmsprop": "torch.optim.RMSprop",
    "sgd": "torch.optim.SGD",
    "lamb": "hyena.src.utils.optim.lamb.JITLamb",
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
    "cosine_warmup_timm": "hyena.src.utils.optim.schedulers.TimmCosineLRScheduler",
}

model = {
    # Backbones from this repo
    "model": "hyena.src.models.sequence.SequenceModel",
    "lm": "hyena.src.models.sequence.long_conv_lm.ConvLMHeadModel",
    "lm_simple": "hyena.src.models.sequence.simple_lm.SimpleLMHeadModel",
    "vit_b_16": "hyena.src.models.baselines.vit_all.vit_base_patch16_224",
}

layer = {
    "id": "hyena.src.models.sequence.base.SequenceIdentity",
    "ff": "hyena.src.models.sequence.ff.FF",
    "mha": "hyena.src.models.sequence.mha.MultiheadAttention",
    "s4d": "hyena.src.models.sequence.ssm.s4d.S4D",
    "s4_simple": "hyena.src.models.sequence.ssm.s4_simple.SimpleS4Wrapper",
    "long-conv": "hyena.src.models.sequence.long_conv.LongConv",
    "h3": "hyena.src.models.sequence.h3.H3",
    "h3-conv": "hyena.src.models.sequence.h3_conv.H3Conv",
    "hyena": "hyena.src.models.sequence.hyena.HyenaOperator",
    "hyena-filter": "hyena.src.models.sequence.hyena.HyenaFilter",
    "vit": "hyena.src.models.sequence.mha.VitAttention",
}

callbacks = {
    "timer": "hyena.src.callbacks.timer.Timer",
    "params": "hyena.src.callbacks.params.ParamsLog",
    "learning_rate_monitor": "pytorch_lightning.callbacks.LearningRateMonitor",
    "model_checkpoint": "pytorch_lightning.callbacks.ModelCheckpoint",
    "early_stopping": "pytorch_lightning.callbacks.EarlyStopping",
    "swa": "pytorch_lightning.callbacks.StochasticWeightAveraging",
    "rich_model_summary": "pytorch_lightning.callbacks.RichModelSummary",
    "rich_progress_bar": "pytorch_lightning.callbacks.RichProgressBar",
    "progressive_resizing": "hyena.src.callbacks.progressive_resizing.ProgressiveResizing",
}
