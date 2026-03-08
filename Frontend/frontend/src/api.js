import axios from "axios";

export const fetchProducts = async (limit = 100) => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/products`);
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};