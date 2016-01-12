my Game $twixt .= new(
    board => (
        type => Board::SquareGrid::Struts.new(
            hole => my $hole,
            strut => my $strut),
        size => 24,
    ),
    pieces => [Piece::Pin, Piece::Strut],
    rules => {
        .restrict(Piece::Pin).to($hole);
        .restrict(Piece::Strut).to($strut).and(.connectingFriendlies);
    },
);
