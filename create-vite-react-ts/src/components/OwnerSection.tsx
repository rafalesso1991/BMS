interface Props {
    title: string,
    children: React.ReactNode
}
const OwnerSection = ({title, children}: Props) => {
    return (
        <section className="OwnerSection">
            <div className="User">{title}</div>
            <div className="OwnedBooks">{children}</div>
        </section>
    )
};
export default OwnerSection;