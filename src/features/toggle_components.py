def disable_components(window):
    window.btn_calculate.setDisabled(True)
    window.line_result.setDisabled(True)
    window.rb_data_segregation.setDisabled(True)
    window.rb_linear_regression.setDisabled(True)
    window.rb_mean.setDisabled(True)
    window.rb_standard_deviation.setDisabled(True)
    window.rb_time_series.setDisabled(True)
    window.rb_weighted_average.setDisabled(True)

def enable_components(window):
    window.btn_calculate.setDisabled(False)
    window.line_result.setDisabled(False)
    window.rb_data_segregation.setDisabled(False)
    window.rb_linear_regression.setDisabled(False)
    window.rb_mean.setDisabled(False)
    window.rb_standard_deviation.setDisabled(False)
    window.rb_time_series.setDisabled(False)
    window.rb_weighted_average.setDisabled(False)