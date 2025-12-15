import streamlit as st
import json
import os

st.set_page_config(page_title="Tamari Bank", layout="centered")

FILE_NAME = "bank_data.json"

# ---------- Load / Save ----------
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

bank_data = load_data()

# ---------- App ----------
st.title("🏦 Tamari Bank System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create Account", "Deposit Money", "Withdraw Money", "Check Balance", "Update Account", "Delete Account"]
)

# ---------- CREATE ACCOUNT ----------
if menu == "Create Account":
    st.header("Create Account")
    acc_no = st.text_input("Account Number")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    aadhar = st.text_input("Aadhar Number")
    balance = st.number_input("Opening Balance", min_value=0)

    if st.button("Create Account"):
        if acc_no in bank_data:
            st.error("Account already exists")
        else:
            bank_data[acc_no] = {
                "name": name,
                "age": age,
                "aadhar_no": aadhar,
                "balance": balance
            }
            save_data(bank_data)
            st.success("Account Created Successfully")

# ---------- DEPOSIT ----------
elif menu == "Deposit Money":
    st.header("Deposit Money")
    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if acc_no not in bank_data:
            st.error("Account Not Found")
        else:
            bank_data[acc_no]["balance"] += amount
            save_data(bank_data)
            st.success(f"Total Balance: {bank_data[acc_no]['balance']}")

# ---------- WITHDRAW ----------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")
    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if acc_no not in bank_data:
            st.error("Account Not Found")
        elif amount > bank_data[acc_no]["balance"]:
            st.error("Insufficient Balance")
        else:
            bank_data[acc_no]["balance"] -= amount
            save_data(bank_data)
            st.success(f"Remaining Balance: {bank_data[acc_no]['balance']}")

# ---------- CHECK BALANCE ----------
elif menu == "Check Balance":
    st.header("Check Balance")
    acc_no = st.text_input("Account Number")

    if st.button("Check"):
        if acc_no not in bank_data:
            st.error("Account Not Found")
        else:
            st.info(f"Balance: {bank_data[acc_no]['balance']}")

# ---------- UPDATE ACCOUNT ----------
elif menu == "Update Account":
    st.header("Update Account")
    acc_no = st.text_input("Account Number")

    if acc_no in bank_data:
        name = st.text_input("New Name", bank_data[acc_no]["name"])
        age = st.number_input("New Age", min_value=1, value=bank_data[acc_no]["age"])
        aadhar = st.text_input("New Aadhar", bank_data[acc_no]["aadhar_no"])

        if st.button("Update"):
            bank_data[acc_no]["name"] = name
            bank_data[acc_no]["age"] = age
            bank_data[acc_no]["aadhar_no"] = aadhar
            save_data(bank_data)
            st.success("Account Updated Successfully")

# ---------- DELETE ACCOUNT ----------
elif menu == "Delete Account":
    st.header("Delete Account")
    acc_no = st.text_input("Account Number")

    if st.button("Delete"):
        if acc_no not in bank_data:
            st.error("Account Not Found")
        else:
            del bank_data[acc_no]
            save_data(bank_data)
            st.success("Account Deleted Successfully")
