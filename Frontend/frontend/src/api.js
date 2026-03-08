import axios from "axios";

// Base URL for your FastAPI backend
const API_BASE = "http://127.0.0.1:8000";

export const fetchProducts = async () => {
  const res = await axios.get(`${API_BASE}/products?limit=1000`);
  return res.data;
};

export const fetchCategories = async () => {
  const res = await axios.get(`${API_BASE}/categories`);
  return res.data;
};