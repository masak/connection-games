my Game $druid .= new(
    board => (
        type => Board::SquareGrid::Stacking.new(
            surface => my $surface,
        ),
        size => 10,
    ),
    pieces => [
        Piece::Sarsen,
        Piece::Lintel,
    ],
    rules => {
        .passing.permit;
        .restrict(Piece::Sarsen).to(.directlyAbove(.friendly));
        .restrict(Piece::Lintel).to(!$surface).and(
            .directlyAbove(2 * .friendly) ||
            .directlyAbove(3 * .friendly));
    },
);
