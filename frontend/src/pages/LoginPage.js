import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

function LoginPage() {
  let { loginUser } = useContext(AuthContext);

  return (
    <div>
      <from onSubmit={loginUser}>
        <input type="text" name="username" placeholder="Enter username" />
        <input type="password" name="password" placeholder="Enter password" />
        <input type="submit" />
      </from>
    </div>
  );
}

export default LoginPage;
