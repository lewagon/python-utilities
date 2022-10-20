from wagon_common.helpers.git.branch import rename_branch, get_current_branch

class TestGitBranchHelper():

    def test_git_branch_renamed(self):
      very_fancy_branch_name = 'very-fancy-branch-3000'
      # get branch name with get_branch_name
      rc, _output, _error, original_branch = get_current_branch(None)
      assert rc == 0

      # rename it to 'very-fancy-branch'
      rc, _output, _error = rename_branch(None, very_fancy_branch_name)
      assert rc == 0

      # get_branch_name to check it matches above
      rc, _output, _error, new_branch = get_current_branch(None)
      assert new_branch == very_fancy_branch_name
      assert rc == 0

      # rename back to whatever was returned originally
      rc, _output, _error = rename_branch(None, original_branch)
      rc, _output, _error, reverted_branch = get_current_branch(None)
      assert rc == 0
      assert reverted_branch == original_branch

