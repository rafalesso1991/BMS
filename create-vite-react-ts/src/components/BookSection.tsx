interface Props {
    title: string,
    children: React.ReactNode
}
const BookSection = ({title, children}: Props) => {
    return (
        <section className="BookSection">
            <div className="BookList">{title}</div>
            <div className="Searcher">{children}</div>
        </section>
    )
};
export default BookSection;