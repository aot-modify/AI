import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
from collections import Counter
from datetime import datetime
import time

st.title("📊 Monthly Histogram of User Inputs (12 Months View)")

if "chat_history" not in st.session_state or len(st.session_state.chat_history) == 0:
    st.warning("❗ No chat history found. Please interact with the chatbot first.")
else:
    current_year = datetime.now().year
    months = [f"{current_year}-{str(m).zfill(2)}" for m in range(1, 13)]

    user_msgs = [c for c in st.session_state.chat_history if c["sender"] == "user"]
    monthly_counts = Counter()
    for chat in user_msgs:
        try:
            dt = datetime.strptime(chat["timestamp"], "%Y-%m-%d")
            ym = dt.strftime("%Y-%m")
            monthly_counts[ym] += 1
        except:
            pass

    histogram_data = []
    for ym in months:
        dt = datetime.strptime(ym, "%Y-%m")
        unix_time = int(time.mktime(dt.timetuple()))
        count = monthly_counts.get(ym, 0)
        histogram_data.append({
            "value": count,
            "time": unix_time
        })

    chartOptions = {
        "layout": {
            "textColor": 'black',
            "background": {
                "type": 'solid',
                "color": 'white'
            }
        }
    }

    seriesHistogramChart = [{
        "type": 'Histogram',
        "data": histogram_data,
        "options": { "color": '#26a69a' }
    }]

    st.subheader("📅 Histogram: User Inputs per Month (All 12 Months)")
    renderLightweightCharts([{
        "chart": chartOptions,
        "series": seriesHistogramChart
    }], 'histogram')

    st.write("### 📋 Monthly Summary")
    for entry in histogram_data:
        date_str = datetime.utcfromtimestamp(entry["time"]).strftime("%B")
        st.write(f"{date_str}: {entry['value']} message(s)")
