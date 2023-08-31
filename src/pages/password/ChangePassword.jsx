import "./changepassword.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbar/Navbar";

import React, { useState } from "react";
import { auth } from "../../firebase";
import { EmailAuthProvider, updatePassword } from "firebase/auth";
import FormInput from "../../components/forminput/FormInput";

import { toast, Toaster } from "react-hot-toast";
import { useNavigate } from "react-router-dom";
import CircularProgress from "@mui/material/CircularProgress";

const ChangePassword = () => {
  const [values, setValues] = useState({
    password: "",
    confirmPassword: "",
  }); // Handle multiple input at once
  const [changingPassword, setChangingPassword] = useState(false); // Spinner icon
  const [errorMsg, setErrorMsg] = useState(""); // Error msg on register

  const navigate = useNavigate();

  const formInputs = [
    {
      id: 1,
      name: "password",
      type: "password",
      placeholder: "New Password",
      errorMessage:
        "Password should be 8-20 characters and include at least 1 letter, 1 number and 1 special character!",
      label: "New Password",
      pattern: `^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,20}$`,
      required: true,
    },
    {
      id: 2,
      name: "confirmPassword",
      type: "password",
      placeholder: "Confirm Password",
      errorMessage: "Passwords don't match!",
      label: "Confirm Password",
      pattern: values.password,
      required: true,
    },
  ];

  const handleChangePassword = async (e) => {
    e.preventDefault(); // This is to prevent refreshing
    setChangingPassword(true);

    try {
      const user = auth.currentUser;

      if (!user) {
        // setError("User not authenticated."); // Handle the case where user is not authenticated
        console.log("User not authenticated from firebase.");
        toast.error("User not authenticated.");
        setChangingPassword(false);
        return;
      }

      // Re-authenticate user with current password before changing it
      EmailAuthProvider.credential(
        user.email,
        values.password
      );      
      // const credentials = EmailAuthProvider.credential(
      //   user.email,
      //   values.password
      // );
      // await reauthenticateWithCredential(user, credentials);

      // Update password
      await updatePassword(user, values.password); // Use auth.updatePassword()
      console.log("Password updated successfully");
      toast.success("Password updated successfully!");
      setTimeout(() => {
        navigate(-1);
      }, 3000);
      setChangingPassword(false);
    } catch (error) {
      setErrorMsg(error.message);
      console.error("Error changing password:", error);
      toast.error("Error changing password:", error);
      setTimeout(() => {
        navigate(-1);
      }, 3000);
      setChangingPassword(false);
    }
  };

  const onChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };

  return (
    <div className="changePassword">
      <Sidebar />
      <div className="changePasswordContainer">
        <Toaster toastOptions={{ duration: 3000 }} />
        <Navbar />
        <form onSubmit={handleChangePassword}>
          <h1>Change Password</h1>
          {formInputs.map((formInput) => {
            return (
              <FormInput
                key={formInput.id}
                {...formInput}
                values={values[formInput.name]}
                onChange={onChange}
              />
            );
          })}
          <button>
            {changingPassword ? ( // changingPassword (true) = spinner will appear
              <CircularProgress color="inherit" size={20} />
            ) : (
              "Change Password"
            )}
          </button>
          <span className="changePasswordErr">{errorMsg}</span>
        </form>
      </div>
    </div>
  );
};

export default ChangePassword;
