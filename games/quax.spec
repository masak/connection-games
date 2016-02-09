my Game $quax .= new(
    grid => (
        type => Grid::Octagon::Tiling.new(
            octagon => my $octagon,
            diamond => my $diamond,
        ),
        defaultSize => 11,
    ),
    pieces => [Piece::Stone, Piece::Bridge],
    rules => {
        .restrict(Piece::Stone).to($octagon);
        .restrict(Piece::Bridge).to($diamond).and(.connectingFriendlies);
    },
);
