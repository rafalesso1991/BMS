import React, { createContext, useState } from "react";

const AuthContext = createContext({ token: null });

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({});
    const [token, setToken] = useState(null);

    return (
        <AuthContext.Provider value = { { auth, setAuth, token, setToken } }>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthContext;
