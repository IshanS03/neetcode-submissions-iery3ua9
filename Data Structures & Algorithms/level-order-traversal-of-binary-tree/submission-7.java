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
    public List<List<Integer>> levelOrder(TreeNode root) {

        if(root == null){
            return new ArrayList<>();
        }
        
        //multiplies by 2 at each level
        int size = 1;
        List<List<Integer>> res = new ArrayList<>();
        //BFS
        Deque<TreeNode> bfs = new LinkedList<TreeNode>();
        bfs.add(root);
        while(bfs.peek() != null){
            
            List<Integer> level = new ArrayList<>();
            size = bfs.size();
            for(int i = 0; i<size; i++){

                TreeNode temp = bfs.poll();
                level.add(temp.val);

                if(temp.left != null){
                    bfs.add(temp.left);
                }

                if(temp.right != null){
                    bfs.add(temp.right);
                }

            }
            res.add(level);

        }

        return res;

        
    }
}
