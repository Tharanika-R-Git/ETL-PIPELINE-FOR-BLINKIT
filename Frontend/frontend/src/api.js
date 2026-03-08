import axios from "axios";

export const fetchProducts = async (limit = 100) => {
  try {
    const response = await axios.get(`https://ackend-tharanika-r-git7566-o5x6v5ff.leapcell.dev/products`);
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};