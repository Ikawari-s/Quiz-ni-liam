import React from "react";
import Header from "./components/Header";
import Homescreen from './screens/Homescreen';
import "./bootstrap.min.css";
import { Container } from "react-bootstrap";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Productscreen from "./screens/Productscreen";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import CartScreen from "./screens/CartScreen";

// need mag kakasunod amp

function App() {
  return (
    <Router>
      <Header />
        <Container>
          <Routes>
            <Route path='/login' element={<LoginScreen />} />
            <Route path= '/cart' element={<CartScreen/>}/>
            <Route path='/register' element={<RegisterScreen />} />
            <Route path = "/" element={<Homescreen />} exact />
            <Route path = "/product/:id" element= {<Productscreen />} />

          </Routes>
        </Container>
    </Router>
  );
}

export default App;
