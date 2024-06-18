<h2><a href="https://leetcode.com/problems/repeat-string/">2796. Repeat String</a></h2><h3>Easy</h3><hr><div><p>Write code that enhances all strings such that you can call the&nbsp;<code>string.replicate(x)</code>&nbsp;method on any string and it will return repeated string <code>x</code> times.</p>

<p>Try to implement it without using the built-in method <code>string.repeat</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> str = "hello", times = 2
<strong>Output:</strong> "hellohello"
<strong>Explanation:</strong> "hello" is repeated 2 times
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> str = "code", times = 3
<strong>Output:</strong> "codecodecode"
<strong>Explanation:</strong> "code" is repeated 3 times
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 3:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> str = "js", times = 1
<strong>Output:</strong> "js"
<strong>Explanation:</strong> "js" is repeated 1 time
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= times &lt;=&nbsp;10<sup>5</sup></code></li>
	<li><code>1 &lt;=&nbsp;str.length &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Let's assume, for the sake of simplifying analysis, that concatenating strings is a constant time operation <code>O(1)</code>. With this assumption in mind, can you write an algorithm with a runtime complexity of <code>O(log n)</code>?</div>