import numpy as np

def satellite_image2rgb_image(satellite_image, bands=[3,2,1], quantiles=[0.001, 0.999]):
    '''
    satellite_image - 3D numpy array ROWS x COLS x CHANNELS
    bands - list of bands. bands[0] -> red channel, bands[1] -> green channel, bands[2] -> blue channel
    quantiles - quantiles for clipping band
    '''
    h, w, c = satellite_image.shape
    rgb_image = []
    for band in bands:
        channel = satellite_image[:, :, band]
        channel_quantiles = np.quantile(channel, quantiles)
        channel = np.clip(channel, *channel_quantiles)
        channel = ((channel - channel.min()) / (channel.max() - channel.min()) * 255)
        channel = channel.astype(np.uint8)
        channel = channel.reshape(h, w, 1)
        rgb_image.append(channel)
    return np.concatenate(rgb_image, axis=2)
