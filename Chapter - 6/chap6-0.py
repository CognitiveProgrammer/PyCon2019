new_y = np.array([])
slope_m = 1.42
b_intercept = 4.32

for X_value in X_Distance:
    y_val = (X_value * slope_m) + b_intercept
    new_y = np.append(new_y,[y_val])

new_y = new_y.reshape(5,-1)