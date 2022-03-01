import axios from "axios";

const baseURL = process.env.REACT_APP_SERVER_URL;

export const fetchAPI = async (endpoint, method, params) => {
  if (endpoint[0] !== "/") {
    endpoint = "/" + endpoint;
  }

  const config = {
    method: method,
    url: `${baseURL}${endpoint}`,
    params,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  };

  try {
    const res = await axios(config)
    return res.data;
  } catch (err) {
    throw err;
  }
};
