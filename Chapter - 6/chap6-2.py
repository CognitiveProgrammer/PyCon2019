y_end = 43000
y_begin = 200000

X_end = 120
X_begin = 0

slope_m = (y_end - y_begin) / (X_end - X_begin)

print("Slope => ", slope_m)

# (y - y1) = m(X - x1)

# y - 200000 = -1308.33(X - 0)

# y - 200000 = -1308X + 0

# y = -1308X + 200000

b_intercept = 200000

print("b_Intercept => ", b_intercept)

new_y = np.array([])

for X_value in X_property_distance_from_downtown:
    y_val = (X_value * slope_m) + b_intercept
    new_y = np.append(new_y,[y_val])

new_y = new_y.reshape(6,-1)

mse_new = mean_squared_error(y_property_price, new_y)

print("Mean Squared Error => ", mse_new)
print("Mean Squared Error by LR => ", mse)

plt.xlabel("Distance in Miles from Downtown")
plt.ylabel("Price at the location")
plt.plot(X_property_distance_from_downtown, y_property_price, "r*--")
plt.plot(X_property_distance_from_downtown, y_price_prdict, "g*--")
plt.plot(X_property_distance_from_downtown, new_y, "b*--")