my Game $twixt .= new(
    grid => (
        type => Grid::Square::Struts.new(
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
