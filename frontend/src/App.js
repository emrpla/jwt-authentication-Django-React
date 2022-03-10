import "./App.css";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PrivateRoute from "./utils/PrivateRoute";
import { AuthProvider } from "./context/AuthContext";

import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import Header from "./components/Header";

function App() {
  const rootElement = document.getElementById("root");
  render(
    <BrowserRouter>
      <AuthProvider>
        <Header />
        <Routes>
          <Route exact path="/" element={<PrivateRoute />}>
            <Route exact path="/" element={<HomePage />} />
          </Route>
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </AuthProvider>
    </BrowserRouter>,
    rootElement
  );
}

export default App;
