my Game $antipod .= new(
    board => (
        type => Board::SphereOfHexagons,
        size => 6,
        initial => Initial::Antipod.new(
            blackGoal1 => my $goal1,
            blackGoal2 => my $goal2,
        ),
    ),
    pieces => [Piece::Stone],
    rules => {
        .winFor(Player::Black).when(.connected($goal1, $goal2));
        .winFor(Player::White).when(.unconnectable($goal1, $goal2));
    },
);
