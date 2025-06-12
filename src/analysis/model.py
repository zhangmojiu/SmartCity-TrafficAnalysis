# 暂时为空，后续若有模型构建（如LSTM、GRU）需求时补充
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units = 50, return_sequences = True, input_shape = input_shape))
    model.add(LSTM(units = 50))
    model.add(Dense(units = 1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model