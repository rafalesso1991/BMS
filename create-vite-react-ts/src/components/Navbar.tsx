import { useEffect, useState } from "react";
import NavbarSection from "./NavBarSection";
const Navbar = () => {
    const INITIAL_STATE = [
        {
          id: 1,
          username: 'rafael',
          admin: true,
          avatar: 'https://i.pravatar.cc/150?u=rafael'
        },
        {
          id: 2,
          username: 'lunavioleta',
          admin: false,
          avatar: 'https://i.pravatar.cc/150?u=lunavioleta'
        }
    ]
    interface User {
        id: number
        username: string
        admin: boolean
        avatar: string
    }
    interface NavbarState {
        users: User[]
    }
    const [users, setUsers] = useState<NavbarState["users"]>([])
    useEffect(() => {
        setUsers(INITIAL_STATE)
    }, [])
    return (
        <NavbarSection title="Username">
            <ul>
                {users.map(user => {
                    return (
                        <li key={user.id}>
                            <h4>{user.username}</h4>
                            <img src={user.avatar} alt={'${user.username} avatar'} />
                        </li>
                    )
                })}
            </ul>
            <button type="submit">Logout</button>
        </NavbarSection>
    )
};
export default Navbar;