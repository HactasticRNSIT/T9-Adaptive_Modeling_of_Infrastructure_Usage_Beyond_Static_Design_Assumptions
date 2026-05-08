import joblib
import pandas as pd

def get_ai_prediction(time_slot, day_type):
    try:
        # Load the trained AI Brain
        model = joblib.load("urban_pulse_model.pkl")
        
        # Prepare the input (Encoding must match the trainer)
        time_map = {"Morning": 0, "Afternoon": 1, "Evening": 2}
        day_map = {"Normal": 0, "Festival": 1}
        
        input_data = [[time_map.get(time_slot, 0), day_map.get(day_type, 0)]]
        
        # Get the AI's prediction
        prediction = model.predict(input_data)[0]
        return f"{prediction:.1f}%"
    except:
        return "Calculating..." # Fallback if model isn't trained yet