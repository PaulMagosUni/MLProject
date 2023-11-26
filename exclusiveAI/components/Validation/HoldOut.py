from exclusiveAI.utils import train_split
from exclusiveAI.ConfiguratorGen import ConfiguratorGen


class HoldOut:
    def __init__(self, models: ConfiguratorGen, input, target, split_size=0.2, shuffle=True, seed=42,
                 assessment: bool = False):
        self.best_model = None
        self.best_config = None
        self.models = models
        self.input = input
        self.target = target
        self.split_size = split_size
        self.shuffle = shuffle
        self.seed = seed
        self.assessment = assessment

    def hold_out(self):
        metric = 'val_mse' if self.assessment else 'mse'
        train, train_target, validation, validation_target, _, _ = train_split(inputs=self.input,
                                                                                     input_label=self.target,
                                                                                     split_size=self.split_size,
                                                                                     shuffle=self.shuffle,
                                                                                     random_state=self.seed)
        for model, config in self.models:
            model.train(train, train_target, None if self.assessment else validation,
                        None if self.assessment else validation_target)
            if self.best_model is None:
                self.best_model = model
                self.best_config = config
            else:
                if model.get_last()[metric] < self.best_model.get_last()[metric]:
                    self.best_model = model
                    self.best_config = config
        return self.best_model.evaluate(validation, validation_target) if self.assessment else self.best_config
