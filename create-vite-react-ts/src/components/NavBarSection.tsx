interface Props {
    title: string,
    children: React.ReactNode
}
const NavbarSection = ({children}: Props) => {
    return (
        <section className="NavbarSection">
            <div className="Button">{children}</div>
        </section>
    )
};
export default NavbarSection;