scp_bb(Set):
    local_cost = ∞
    current_best = random()
    while (Set != null):
        Choose an element c from the Set
        Remove c from Set
        Branching into subproblems {ci , i = 1, ...l}
        for (i = 1; i <= 1; i++):
            lb = lower_limit(ci )
            if (lb ≥ local_cost):
                ci.kill()
            else:
            if (ci is complete solution):
            best_current = c
            local_cost = ci .cost()
    else:
        Set.add(ci)
