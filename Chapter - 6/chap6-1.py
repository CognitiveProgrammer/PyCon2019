prop_lreg = LinearRegression()

prop_lreg.fit(X_property_distance_from_downtown, y_property_price)

y_price_prdict = prop_lreg.predict(X_property_distance_from_downtown)

mse = mean_squared_error(y_property_price, y_price_prdict)
print("Mean Sqared Error => ", mse)
print("slope and Intercept => ", prop_lreg.coef_, prop_lreg.intercept_ )