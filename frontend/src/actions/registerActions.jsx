import axios from 'axios';
import {
  USER_REGISTER_REQUEST,
  USER_REGISTER_SUCCESS,
  USER_REGISTER_FAIL,
} from "../constants/registerConstants";

export const register = (name, email, password) => async (dispatch) => {
  try {
    dispatch({ type: USER_REGISTER_REQUEST });
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };
    const { data } = await axios.post(
      "http://127.0.0.1:8000/api/users/register/",
      { name, email, password },
      config
    );
    dispatch({
      type: USER_REGISTER_SUCCESS,
      payload: data,
    });
    // localStorage.setItem("userInfo", JSON.stringify(data)); 
  } catch (error) {
    dispatch({
      type: USER_REGISTER_FAIL,
      payload:  
        error.response && error.response.data.details
          ? error.response.data.details
          : error.message,
    });
  }
};
