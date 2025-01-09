# # from keras import layers, models
# # from keras.applications import MobileNetV2, EfficientNetB0
# # from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, GlobalAveragePooling2D

# import tensorflow as tf
# from tensorflow.keras import layers, models
# from tensorflow.keras.applications import MobileNetV2, EfficientNetB0
# from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, GlobalAveragePooling2D


# def build_model(input_shapes):
#     """
#     Builds a multi-input model for predicting controls using multiple modalities,
#     applying transfer learning to RGB images and segmentation masks.

#     Parameters:
#     - input_shapes: Dictionary of input shapes for each modality.

#     Returns:
#     - model: A Keras model.
#     """
#     inputs = []

#     # RGB images input with Transfer Learning (MobileNetV2)
#     rgb_input = Input(shape=input_shapes['rgb'], name="rgb")
#     base_rgb_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=input_shapes['rgb'])
#     base_rgb_model.trainable = False  # Freeze the pre-trained layers
#     rgb_branch = base_rgb_model(rgb_input)
#     rgb_branch = GlobalAveragePooling2D()(rgb_branch)
#     rgb_branch = Dense(64, activation='relu')(rgb_branch)
#     inputs.append(rgb_input)

#     # Segmentation masks input with Transfer Learning (EfficientNetB0)
#     segmentation_input = Input(shape=input_shapes['segmentation'], name="segmentation")
#     base_seg_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=input_shapes['segmentation'])
#     base_seg_model.trainable = False  # Freeze the pre-trained layers
#     segmentation_branch = base_seg_model(segmentation_input)
#     segmentation_branch = GlobalAveragePooling2D()(segmentation_branch)
#     segmentation_branch = Dense(64, activation='relu')(segmentation_branch)
#     inputs.append(segmentation_input)

#     # High-Level Command input (HLC) - Direct input without transfer learning
#     hlc_input = Input(shape=input_shapes['hlc'], name="hlc")
#     hlc_branch = Dense(64, activation='relu')(hlc_input)
#     inputs.append(hlc_input)

#     # Traffic Light Status input - Direct input without transfer learning
#     light_input = Input(shape=input_shapes['light'], name="light")
#     light_branch = Dense(64, activation='relu')(light_input)
#     inputs.append(light_input)

#     # Measurements input (speed) - Direct input without transfer learning
#     measurements_input = Input(shape=input_shapes['measurements'], name="measurements")
#     measurements_branch = Dense(64, activation='relu')(measurements_input)
#     inputs.append(measurements_input)

#     # Concatenate all branches
#     concatenated = layers.concatenate([rgb_branch, segmentation_branch, hlc_branch, light_branch, measurements_branch])

#     # Output layer (for control predictions)
#     output = Dense(3, activation='tanh', name="controls")(concatenated)

#     # Define the model
#     model = models.Model(inputs=inputs, outputs=output)
#     # model.compile(optimizer='adam', loss='mse', metrics=['mae'])

#     return model
# from keras import layers, models
# from keras.applications import MobileNetV2, EfficientNetB0
# from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, GlobalAveragePooling2D

import tensorflow as tf
from tensorflow.keras import regularizers
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2, EfficientNetB0
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, GlobalAveragePooling2D
import tensorflow as tf
from tensorflow.keras import layers, models

# def build_model(input_shapes):
#     """
#     A simpler model using only CNN layers for RGB and segmentation inputs.
#     """

#     # RGB images input
#     rgb_input = layers.Input(shape=input_shapes['rgb'], name="rgb")
#     rgb_branch = layers.Conv2D(32, (3, 3), activation='relu')(rgb_input)
#     rgb_branch = layers.MaxPooling2D((2, 2))(rgb_branch)
#     rgb_branch = layers.Conv2D(64, (3, 3), activation='relu')(rgb_branch)
#     rgb_branch = layers.MaxPooling2D((2, 2))(rgb_branch)
#     rgb_branch = layers.Conv2D(128, (3, 3), activation='relu')(rgb_branch)
#     rgb_branch = layers.MaxPooling2D((2, 2))(rgb_branch)
#     rgb_branch = layers.Flatten()(rgb_branch)
#     rgb_branch = layers.Dense(64, activation='relu')(rgb_branch)

#     # Segmentation masks input
#     segmentation_input = layers.Input(shape=input_shapes['segmentation'], name="segmentation")
#     segmentation_branch = layers.Conv2D(32, (3, 3), activation='relu')(segmentation_input)
#     segmentation_branch = layers.MaxPooling2D((2, 2))(segmentation_branch)
#     segmentation_branch = layers.Conv2D(64, (3, 3), activation='relu')(segmentation_branch)
#     segmentation_branch = layers.MaxPooling2D((2, 2))(segmentation_branch)
#     segmentation_branch = layers.Conv2D(128, (3, 3), activation='relu')(segmentation_branch)
#     segmentation_branch = layers.MaxPooling2D((2, 2))(segmentation_branch)
#     segmentation_branch = layers.Flatten()(segmentation_branch)
#     segmentation_branch = layers.Dense(64, activation='relu')(segmentation_branch)

#     # HLC, Light, and Measurements inputs
#     hlc_input = layers.Input(shape=input_shapes['hlc'], name="hlc")
#     hlc_branch = layers.Dense(64, activation='relu')(hlc_input)

#     light_input = layers.Input(shape=input_shapes['light'], name="light")
#     light_branch = layers.Dense(64, activation='relu')(light_input)

#     measurements_input = layers.Input(shape=input_shapes['measurements'], name="measurements")
#     measurements_branch = layers.Dense(64, activation='relu')(measurements_input)

#     # Concatenate all branches
#     concatenated = layers.concatenate([rgb_branch, segmentation_branch, hlc_branch, light_branch, measurements_branch])

#     # Output layer for controls
#     throttle_output = layers.Dense(1, activation='sigmoid', name="throttle")(concatenated)
#     steering_output = layers.Dense(1, activation='tanh', name="steering")(concatenated)
#     brake_output = layers.Dense(1, activation='sigmoid', name="brake")(concatenated)

#     # Model
#     model = models.Model(inputs=[rgb_input, segmentation_input, hlc_input, light_input, measurements_input], 
#                          outputs=[throttle_output, steering_output, brake_output])

#     return model

from tensorflow.keras import layers, models, regularizers

def build_model(input_shapes):
    """
    FL-compatible model with L2 regularization and BatchNorm
    """
    # RGB branch
    rgb_input = layers.Input(shape=input_shapes['rgb'], name="rgb")
    rgb_branch = layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01))(rgb_input)
    rgb_branch = layers.BatchNormalization()(rgb_branch)
    rgb_branch = layers.MaxPooling2D((2, 2))(rgb_branch)
    rgb_branch = layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01))(rgb_branch)
    rgb_branch = layers.BatchNormalization()(rgb_branch)
    rgb_branch = layers.MaxPooling2D((2, 2))(rgb_branch)
    rgb_branch = layers.Flatten()(rgb_branch)
    rgb_branch = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(rgb_branch)
    
    # Segmentation branch
    segmentation_input = layers.Input(shape=input_shapes['segmentation'], name="segmentation")
    segmentation_branch = layers.Conv2D(16, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01))(segmentation_input)
    segmentation_branch = layers.BatchNormalization()(segmentation_branch)
    segmentation_branch = layers.MaxPooling2D((2, 2))(segmentation_branch)
    segmentation_branch = layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01))(segmentation_branch)
    segmentation_branch = layers.BatchNormalization()(segmentation_branch)
    segmentation_branch = layers.MaxPooling2D((2, 2))(segmentation_branch)
    segmentation_branch = layers.Flatten()(segmentation_branch)
    segmentation_branch = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(segmentation_branch)

    # Other inputs
    hlc_input = layers.Input(shape=input_shapes['hlc'], name="hlc")
    hlc_branch = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(hlc_input)

    light_input = layers.Input(shape=input_shapes['light'], name="light")
    light_branch = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(light_input)

    measurements_input = layers.Input(shape=input_shapes['measurements'], name="measurements")
    measurements_branch = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(measurements_input)

    # Final layers
    concatenated = layers.concatenate([rgb_branch, segmentation_branch, hlc_branch, light_branch, measurements_branch])
    concatenated = layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01))(concatenated)

    # Outputs
    throttle_output = layers.Dense(1, activation='sigmoid', name="throttle")(concatenated)
    steering_output = layers.Dense(1, activation='tanh', name="steering")(concatenated)
    brake_output = layers.Dense(1, activation='sigmoid', name="brake")(concatenated)

    return models.Model(
        inputs=[rgb_input, segmentation_input, hlc_input, light_input, measurements_input],
        outputs=[throttle_output, steering_output, brake_output]
    )