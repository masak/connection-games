my Game $druid .= new(
    grid => (
        type => Grid::Square::Stacking.new(
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
