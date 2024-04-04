import { ReactNode } from "react";

interface Props {
    children: ReactNode
}
const Container = ({children}: Props) => {
    return <main className="Container">
        {children}
    </main>
};
export default Container