%lang starknet

@external
func test_failure{syscall_ptr : felt*, range_check_ptr}():
    assert 1 = 0
    return ()
end
