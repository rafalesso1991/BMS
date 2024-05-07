import axios from "axios";

const BASE_URL = 'http://localhost:8000'; // Base url to make Requests to the BMS-DB

export default axios.create({
    baseURL: BASE_URL
});

export const axiosPrivate = axios.create({
    baseURL: BASE_URL,
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    withCredentials: true
});
