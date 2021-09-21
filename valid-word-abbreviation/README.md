<h2>408. Valid Word Abbreviation</h2><h3>Easy</h3><hr><div><p>A string can be <strong>abbreviated</strong> by replacing any number of <strong>non-adjacent</strong> substrings with their lengths. For example, a string such as <code>"substitution"</code> could be abbreviated as (but not limited to):</p>

<ul>
	<li><code>"s10n"</code> (<code>"s <u>ubstitutio</u> n"</code>)</li>
	<li><code>"sub4u4"</code> (<code>"sub <u>stit</u> u <u>tion</u>"</code>)</li>
	<li><code>"12"</code> (<code>"<u>substitution</u>"</code>)</li>
	<li><code>"su3i1u2on"</code> (<code>"su <u>bst</u> i <u>t</u> u <u>ti</u> on"</code>)</li>
	<li><code>"substitution"</code> (no substrings replaced)</li>
	<li><code>"s010n"</code> (leading zeros in numbers are allowed)</li>
</ul>

<p>Note that <code>"s55n"</code> (<code>"s <u>ubsti</u> <u>tutio</u> n"</code>) is not a valid abbreviation of <code>"substitution"</code> because the replaced substrings are adjacent.</p>

<p>Given a string <code>word</code> and an abbreviation <code>abbr</code>, return <em>whether the string <strong>matches</strong> with the given abbreviation</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> word = "internationalization", abbr = "i12iz4n"
<strong>Output:</strong> true
<strong>Explanation:</strong> The word "internationalization" can be abbreviated as "i12iz4n" ("i <u>nternational</u> iz <u>atio</u> n").
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> word = "apple", abbr = "a2e"
<strong>Output:</strong> false
<strong>Explanation:</strong> The word "apple" cannot be abbreviated as "a2e".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 20</code></li>
	<li><code>word</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= abbr.length &lt;= 10</code></li>
	<li><code>abbr</code> consists of lowercase English letters and digits.</li>
	<li>All the integers in <code>abbr</code> will fit in a 32-bit integer.</li>
</ul>
</div>