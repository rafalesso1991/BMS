import React, { useState, useContext } from "react";
import { Context } from "../App"

export default function Btn() {

    const [login, setLogin] = useContext(Context)

    return (
    <Button variant="contained" color="primary" onClick = { () => setLogin(!login) }>
        { login ? 'Login' : 'Logout' }
    </Button>
    )
}