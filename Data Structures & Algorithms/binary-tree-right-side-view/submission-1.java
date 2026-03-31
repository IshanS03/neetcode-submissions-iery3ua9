/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    ArrayList<Integer> res = new ArrayList<>();
    HashMap<Integer, Integer> level = new HashMap<>();
    int height = 0;

    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, 0);
        for(int i = 0; i<height; i++){
            res.add(level.get(i));
        }
        return res;
    }

    private void dfs(TreeNode node, int depth){

        if(node == null){
            return;
        }

        if(!level.containsKey(depth)){
            height++;
        }

        level.put(depth, node.val);

        dfs(node.left, depth+1);
        dfs(node.right, depth+1);

    }
}
