import streamlit as st
import pandas as pd
from datetime import datetime

# Example data: doctors' schedules and info
def psikolog():
    doctors = {
        'Doctor ID': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4],
        'Name': ['Dr. Ahmad Fauzi', 'Dr. Ahmad Fauzi', 'Dr. Ahmad Fauzi', 
                'Dr. Siti Aminah', 'Dr. Siti Aminah', 'Dr. Siti Aminah', 
                'Dr. Budi Santoso', 'Dr. Budi Santoso', 'Dr. Budi Santoso', 
                'Dr. Ratna Dewi', 'Dr. Ratna Dewi', 'Dr. Ratna Dewi'],
        'Gender': ['Male', 'Male', 'Male', 'Female', 'Female', 'Female', 
                'Male', 'Male', 'Male', 'Female', 'Female', 'Female'],
        'Availability': [
            '2024-07-03 10:00', '2024-07-03 11:00', '2024-07-03 12:00',
            '2024-07-04 14:00', '2024-07-04 15:00', '2024-07-04 16:00',
            '2024-07-05 09:00', '2024-07-05 10:00', '2024-07-05 11:00',
            '2024-07-06 13:00', '2024-07-06 14:00', '2024-07-06 15:00'
        ]
    }

    doctors_df = pd.DataFrame(doctors)
    doctors_df['Availability'] = pd.to_datetime(doctors_df['Availability'])

    # Streamlit app
    st.title("Book a Mental Health Consultation")

    # Input user details
    first_name = st.text_input('First Name:')
    last_name = st.text_input('Last Name:')
    user_gender = st.selectbox('Your Gender:', ['Male', 'Female', 'Other'])

    # Choose doctor
    doctor = st.selectbox('Choose a doctor:', doctors_df['Name'].unique())

    # Get the doctor's available times
    selected_doctor_info = doctors_df[doctors_df['Name'] == doctor]
    available_times = selected_doctor_info['Availability'].dt.strftime('%Y-%m-%d %H:%M')

    # Choose date and time
    date_time = st.selectbox('Choose a date and time:', available_times)

    # Submit button
    if st.button('Submit'):
        if first_name and last_name and user_gender and doctor and date_time:
            # Here you can add logic to store the appointment details in a database or send an email.
            st.success(f'Appointment booked successfully for {first_name} {last_name} with {doctor} on {date_time}. A confirmation has been sent to your email.')
        else:
            st.error('Please fill in all the details.')



