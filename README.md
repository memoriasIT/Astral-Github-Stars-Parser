<h2>The problem</h2>

<p>
If you are a someone who uses github stars a lot for getting inspiration or just stumble with a lot of interesting ideas you would probably have hundreds of stars.
</p>

<p>The first idea I had was to create a database and manage the stars with tags, however, I thought that someone would have already done that, and that's where my adventure starts.</p>

<h2>The Solution</h2>

<p><a href="https://app.astralapp.com">Astral</a> is a free service that does basically what I just said, It syncs with your github account and is able to see your stars. <br>
There, you are able to use options such as search, tags...</p>

<p><img src="https://i.imgur.com/XQrUU6z.png" alt="walking"></p>


<p>As you can see the website is very appealing and does everything I wanted: You have tags <code>(1)</code>, you can see the repos whitout tags <code>(2)</code>, you can see the readme in case you forgot what that repo was <code>(3)</code> and it has a search functionality <code>(4)</code></p>

<h2>But does it really do everything I wanted?</h2>

<p>Not really... There is no share function, so what if we implement it ourselves? }:-)</p>
<p>Astral let's you export your stars as a JSON, I thought that was great! Until I saw the format of the JSON</p>

<pre>
        {% raw %}
"2": {
    "id": 1039967,
    "user_id": 16684,
    "repo_id": 30003816,
    "notes": null,
    "created_at": "2018-08-16 08:53:14",
    "updated_at": "2018-08-16 08:53:14",
    "autotagged_by_topic": 0,
    "tags": [
        {
            "id": 171370,
            "user_id": 16684,
            "name": "unixporn",
            "sort_order": 0,
            "created_at": "2018-08-16 08:53:00",
            "updated_at": "2018-09-12 18:41:06",
            "slug": "unixporn"
        }
    ]
},
{% endraw %}
</pre>

<p>Unless your friend has access to the github api and a lot of time to spare this is not a very convenient way to share your stars with your friends</p>
<p>Let's fix that!</p>

<H2>Solution to the solution!</H2>
<p>Let's use python to read the JSON file and parse it to human readable data. <br>
We need to read the original astral JSON and get the repo name fore every repo id</p>
<p>We are going to need:</p>
<ul>
<li>json   : to navigate and parse the data (Astral and github api)</li>
<li>urllib : to make requests and parse them</li>
<li>pprint : jsons with normal print look awfull</li>
</ul>

<p>First of all we need to read the file, so we use the open() and close() functions:</p>
{% highlight python %}
# Read File 
json_data=open(json_file)
data = json.load(json_data)
json_data.close()
{% endhighlight %}


<p>After that we need to create our output file and save our stars, we can easily do that with this little code:</p>

{% highlight python %}
file = open('OUTPUT', 'w')
# Request 
url = 'https://api.github.com/repositories/'
for x in data:
    try:
        f = urllib.request.urlopen(url+str(data[x]["repo_id"])+"?access_token="+str(Oauth))
        JSON_object = json.loads(f.read().decode('utf-8', errors='replace'))

        out = str(JSON_object["name"])+ " - " + str(JSON_object["full_name"])+" : "+ 
        str(JSON_object["description"])+ "     (" + str(JSON_object["html_url"] + ")\n")

        print(out)
        file.write(out)
    except:
        pass
        
file.close()
{% endhighlight %}

<p>First of all we create the file, then we do requests to the github api with the repo id. <br>
As we can see the repo id was found in <code>astraljson -> x -> repo_id </code>. We also add a Oauth token for the github api because of api limitations (60 per day). </p>

<P>You can get a oauth key here: <a href="https://github.com/settings/tokens">Github Tokens</a> </P>

<p>After that we decode the json file to utf-8 replacing whatever error we find and create a variable <code>out</code> which holds the format for our output file.</p>

<p>Finally we print the output to the terminal and to the file.</p>

<h2>Taking it further</h2>

<p>I also wanted to print the stars tagged with the "unixporn" tag, so I added a couple of lines to check that:</p>

{% highlight python %}
for y in data[x]["tags"]:
        if (y["name"] == "unixporn"):
            found = True
{% endhighlight %}

<p>I created a boolean called <code>found</code> which is used later to determine if the current item needs to be printed or <br>
The output looks something like this:</p>
<pre>
    {% raw %}
    vi3m - nejni-marji/vi3m :  A really basic tool to use vim-style chained keypresses in i3.     (https://github.com/nejni-marji/vi3m)
    powerlevel9k - bhilburn/powerlevel9k : The most awesome Powerline theme for ZSH around!     (https://github.com/bhilburn/powerlevel9k)
    dotfiles - SteffenC/dotfiles : None     (https://github.com/SteffenC/dotfiles)
    dotfiles - djsavvy/dotfiles : None     (https://github.com/djsavvy/dotfiles)
{% endraw %}
</pre>

<p>And we can run the sort command and have something like:</p>

<pre>
    {% raw %}
    art - gawlk/art : :art: A smart theme generator (https://github.com/gawlk/art)
    autorice - UltraNyan/autorice : Graphical utility to edit and manage your config files. (https://github.com/UltraNyan/autorice)
    bin - gawlk/bin : :pineapple: List of scripts that make my life much easier (https://github.com/gawlk/bin)
{% endraw %}
</pre>
<p>If you want to see the full code you can check my github repo with the quick snippet! <br>
<a href="">Github repository link</a>
</p>
