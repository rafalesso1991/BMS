import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import useAuth from "../hooks/useAuth";

const PrivateRoute = () => { // pasándole ciertos parámetros o props podemos bloquear o no la navegación hacia un endpoint
  const { auth } = useAuth();

  if (!auth) {
    return <Navigate to = '' replace />; // Redirect if not authenticated
  }

  return <Outlet />
}

export default PrivateRoute;