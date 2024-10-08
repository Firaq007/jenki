import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import random

# Function to simulate a build process
def run_build():
    time.sleep(2)  # Simulate build time
    return random.choice(["Success", "Failure"])

# Function to simulate test results
def run_tests():
    time.sleep(1)  # Simulate test time
    return {
        "Total": random.randint(50, 100),
        "Passed": random.randint(40, 95),
        "Failed": random.randint(0, 10)
    }

# Function to simulate deployment
def deploy():
    time.sleep(3)  # Simulate deployment time
    return random.choice(["Success", "Failure"])

# Main Streamlit app
def main():
    st.set_page_config(page_title="CI Dashboard", page_icon="🚀", layout="wide")
    st.title("CI Dashboard")

    # Sidebar
    st.sidebar.title("Actions")
    if st.sidebar.button("Run Pipeline"):
        with st.spinner("Running pipeline..."):
            build_status = run_build()
            test_results = run_tests()
            deployment_status = deploy()

        # Display results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Build Status")
            st.metric("Status", build_status, delta=None)

        with col2:
            st.subheader("Test Results")
            st.metric("Total Tests", test_results["Total"])
            st.metric("Passed", test_results["Passed"], delta=test_results["Passed"] - test_results["Failed"])
            st.metric("Failed", test_results["Failed"])

        with col3:
            st.subheader("Deployment")
            st.metric("Status", deployment_status, delta=None)

    # Recent builds
    st.subheader("Recent Builds")
    builds = pd.DataFrame({
        "Build ID": range(1001, 996, -1),
        "Status": [random.choice(["Success", "Failure"]) for _ in range(5)],
        "Timestamp": [datetime.now() - timedelta(hours=i) for i in range(5)]
    })
    st.dataframe(builds)

    # Placeholder for additional features
    st.subheader("Additional Features")
    st.write("Here you could add more features like:")
    st.write("- Detailed test reports")
    st.write("- Code coverage metrics")
    st.write("- Artifact management")
    st.write("- User authentication")

if __name__ == "__main__":
    main()
