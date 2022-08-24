def disable_components(self):
    self.btn_calculate.setDisabled(True)
    self.line_result.setDisabled(True)
    self.rb_data_segregation.setDisabled(True)
    self.rb_linear_regression.setDisabled(True)
    self.rb_mean.setDisabled(True)
    self.rb_standard_deviation.setDisabled(True)
    self.rb_time_series.setDisabled(True)
    self.rb_weighted_average.setDisabled(True)

def enable_components(self):
    self.btn_calculate.setDisabled(False)
    self.line_result.setDisabled(False)
    self.rb_data_segregation.setDisabled(False)
    self.rb_linear_regression.setDisabled(False)
    self.rb_mean.setDisabled(False)
    self.rb_standard_deviation.setDisabled(False)
    self.rb_time_series.setDisabled(False)
    self.rb_weighted_average.setDisabled(False)