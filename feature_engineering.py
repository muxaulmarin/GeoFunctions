def get_subtractions(satellite_image_previous, satellite_image_current, names=None):
    '''
    satellite_image_<...> - 3D numpy array ROWS x COLS x CHANNELS
    names - list of posible subtraction feature names
    '''
    n_channels = satellite_image_previous.shape[2]
    band_names_previous = ['B' + str(i) + '_prev' for i in range(1, 14)]
    band_names_current = ['B' + str(i) + '_curr' for i in range(1, 14)]
    
    satellite_image_previous = satellite_image_previous.reshape(-1, n_channels).astype(np.int64)
    satellite_image_current = satellite_image_current.reshape(-1, n_channels).astype(np.int64)
    
    subtractions = []
    
    if names is None:
        subtractions_names = []
        for prev_col in range(n_channels):
            for curr_col in range(n_channels):
                subtractions_names.append(band_names_previous[prev_col] + '-' + band_names_current[curr_col])
                substraction = satellite_image_previous[:, prev_col] - satellite_image_current[:, curr_col]
                subtractions.append(substraction.reshape(-1, 1))
        for prev_col_1 in range(n_channels):
            for prev_col_2 in range(n_channels):
                if prev_col_1 != prev_col_2:
                    subtractions_names.append(band_names_previous[prev_col_1] + '-' + band_names_previous[prev_col_2])
                    substraction = satellite_image_previous[:, prev_col_1] - satellite_image_previous[:, prev_col_2]
                    subtractions.append(substraction.reshape(-1, 1))
        for curr_col_1 in range(n_channels):
            for curr_col_2 in range(n_channels):
                if curr_col_1 != curr_col_2:
                    subtractions_names.append(band_names_current[curr_col_1] + '-' + band_names_current[curr_col_2])
                    substraction = satellite_image_current[:, curr_col_1] - satellite_image_current[:, curr_col_2]
                    subtractions.append(substraction.reshape(-1, 1))                    
    else:
        subtractions_names = names.copy()
        for prev_col in range(n_channels):
            for curr_col in range(n_channels):
                name = band_names_previous[prev_col] + '-' + band_names_current[curr_col]
                if name in subtractions_names:
                    substraction = satellite_image_previous[:, prev_col] - satellite_image_current[:, curr_col]
                    subtractions.append(substraction.reshape(-1, 1))
        for prev_col_1 in range(n_channels):
            for prev_col_2 in range(n_channels):
                name = band_names_previous[prev_col_1] + '-' + band_names_previous[prev_col_2]
                if name in subtractions_names:
                    substraction = satellite_image_previous[:, prev_col_1] - satellite_image_previous[:, prev_col_2]
                    subtractions.append(substraction.reshape(-1, 1))
        for curr_col_1 in range(n_channels):
            for curr_col_2 in range(n_channels):
                name = band_names_current[curr_col_1] + '-' + band_names_current[curr_col_2]
                if name in subtractions_names:
                    substraction = satellite_image_current[:, curr_col_1] - satellite_image_current[:, curr_col_2]
                    subtractions.append(substraction.reshape(-1, 1))          
    return np.concatenate(subtractions, axis=1), subtractions_names

def get_divisions(satellite_image_previous, satellite_image_current, names=None):
    '''
    satellite_image_<...> - 3D numpy array ROWS x COLS x CHANNELS
    names - list of posible subtraction feature names
    '''
    n_channels = satellite_image_previous.shape[2]
    band_names_previous = ['B' + str(i) + '_prev' for i in range(1, 14)]
    band_names_current = ['B' + str(i) + '_curr' for i in range(1, 14)]
    
    satellite_image_previous = satellite_image_previous.reshape(-1, n_channels).astype(np.int64)
    satellite_image_current = satellite_image_current.reshape(-1, n_channels).astype(np.int64)
    
    divisions = []
    
    if names is None:
        divisions_names = []
        for prev_col in range(n_channels):
            for curr_col in range(n_channels):
                divisions_names.append(band_names_previous[prev_col] + '/' + band_names_current[curr_col])
                division = satellite_image_previous[:, prev_col] / (satellite_image_current[:, curr_col] + 1e-9)
                divisions.append(division.reshape(-1, 1))
                divisions_names.append(band_names_previous[curr_col] + '/' + band_names_current[prev_col])
                division = satellite_image_previous[:, curr_col] / (satellite_image_current[:, prev_col] + 1e-9)
                divisions.append(division.reshape(-1, 1))
        for prev_col_1 in range(n_channels):
            for prev_col_2 in range(n_channels):
                if prev_col_1 != prev_col_2:
                    divisions_names.append(band_names_previous[prev_col_1] + '/' + band_names_previous[prev_col_2])
                    division = satellite_image_previous[:, prev_col_1] / (satellite_image_previous[:, prev_col_2] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
                    divisions_names.append(band_names_previous[prev_col_2] + '/' + band_names_previous[prev_col_1])
                    division = satellite_image_previous[:, prev_col_2] / (satellite_image_previous[:, prev_col_1] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
        for curr_col_1 in range(n_channels):
            for curr_col_2 in range(n_channels):
                if curr_col_1 != curr_col_2:
                    divisions_names.append(band_names_current[curr_col_1] + '/' + band_names_current[curr_col_2])
                    division = satellite_image_current[:, curr_col_1] / (satellite_image_current[:, curr_col_2] + 1e-9)
                    divisions.append(division.reshape(-1, 1)) 
                    divisions_names.append(band_names_current[curr_col_2] + '/' + band_names_current[curr_col_1])
                    division = satellite_image_current[:, curr_col_2] / (satellite_image_current[:, curr_col_1] + 1e-9)
                    divisions.append(division.reshape(-1, 1))  
    else:
        divisions_names = names.copy()
        for prev_col in range(n_channels):
            for curr_col in range(n_channels):
                name = band_names_previous[prev_col] + '/' + band_names_current[curr_col]
                if name in divisions_names:
                    division = satellite_image_previous[:, prev_col] / (satellite_image_current[:, curr_col] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
                    division = satellite_image_previous[:, curr_col] / (satellite_image_current[:, prev_col] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
        for prev_col_1 in range(n_channels):
            for prev_col_2 in range(n_channels):
                name = band_names_previous[prev_col_1] + '/' + band_names_previous[prev_col_2]
                if name in divisions_names:
                    division = satellite_image_previous[:, prev_col_1] / (satellite_image_previous[:, prev_col_2] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
                    division = satellite_image_previous[:, prev_col_2] / (satellite_image_previous[:, prev_col_1] + 1e-9)
                    divisions.append(division.reshape(-1, 1))
        for curr_col_1 in range(n_channels):
            for curr_col_2 in range(n_channels):
                name = band_names_current[curr_col_1] + '/' + band_names_current[curr_col_2]
                if name in divisions_names:
                    division = satellite_image_current[:, curr_col_1] / (satellite_image_current[:, curr_col_2] + 1e-9)
                    divisions.append(division.reshape(-1, 1))   
                    division = satellite_image_current[:, curr_col_2] / (satellite_image_current[:, curr_col_1] + 1e-9)
                    divisions.append(division.reshape(-1, 1))  
    return np.concatenate(divisions, axis=1), divisions_names