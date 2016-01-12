my Game $y .= new(
    board => (
        type => Board::TriangleOfHexagons.new(
            leftEdge => my $leftEdge,
            rightEdge => my $rightEdge,
            bottomEdge => my $bottomEdge,
        ),
        size => 17,
    ),
    pieces => [Piece::Stone],
    rules => {
        .winFor(Player).when(
            .connected($leftEdge, $rightEdge, $bottomEdge));
    },
);