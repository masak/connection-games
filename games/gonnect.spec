my Game $gonnect .= new(
    board => (
        type => Board::SquareGrid.new(
            topEdge => my $topEdge,
            leftEdge => my $leftEdge,
            rightEdge => my $rightEdge,
            bottomEdge => my $bottomEdge,
        ),
        size => 15,
    ),
    pieces => [Piece::Stone],
    rules => {
        .opponentChain.removeIf(!.liberties);
        .suicide.forbid;
        .winFor(Player).when(
            .connected($topEdge, $bottomEdge) ||
            .connected($leftEdge, $rightEdge));
    },
);
