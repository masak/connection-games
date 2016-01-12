my Game $quax .= new(
    board => (
        type => Board::OctagonalTiling.new(
            octagon => my $octagon,
            diamond => my $diamond,
        ),
        size => 11,
    ),
    pieces => [Piece::Stone, Piece::Bridge],
    rules => {
        .restrict(Piece::Stone).to($octagon);
        .restrict(Piece::Bridge).to($diamond).and(.connectingFriendlies);
    },
);
