




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>Raphael.Export/raphael.export.js at master · ElbertF/Raphael.Export</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="ElbertF/Raphael.Export" name="twitter:title" /><meta content="Raphael.Export - Export Raphaël paper objects to SVG." name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/77259?v=2&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/77259?v=2&amp;s=400" property="og:image" /><meta content="ElbertF/Raphael.Export" property="og:title" /><meta content="https://github.com/ElbertF/Raphael.Export" property="og:url" /><meta content="Raphael.Export - Export Raphaël paper objects to SVG." property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="9206D559:4A7F:1CA9AF3:53E10D94" name="octolytics-dimension-request_id" /><meta content="193309" name="octolytics-actor-id" /><meta content="taejoon" name="octolytics-actor-login" /><meta content="a79597ca53f987fa5a076640e27a51c5668820f4db9dcc7e2363329e3f5cf3d9" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="YUk1g/izHnK4bUAfjV5ln3ztpP2mJ+vuL/5RWio8NA6f8rGGxWgSVrYnIX4skBWMpRnb9tjQSOK2FmcJ4BRUuw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-fd0742b595a8a6746dad51a4d1d8b622df6ae906.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-92aa7821e22ae7bb6492942f1fc94b208dbe0e36.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="d83112651b6d8c2bf61c4c39696d7e5c">

      
  <meta name="description" content="Raphael.Export - Export Raphaël paper objects to SVG.">


  <meta content="77259" name="octolytics-dimension-user_id" /><meta content="ElbertF" name="octolytics-dimension-user_login" /><meta content="2807167" name="octolytics-dimension-repository_id" /><meta content="ElbertF/Raphael.Export" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="2807167" name="octolytics-dimension-repository_network_root_id" /><meta content="ElbertF/Raphael.Export" name="octolytics-dimension-repository_network_root_nwo" />

  <link href="https://github.com/ElbertF/Raphael.Export/commits/master.atom" rel="alternate" title="Recent Commits to Raphael.Export:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production linux vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-hotkey="g n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="taejoon"
    data-repo="ElbertF/Raphael.Export"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="ElbertF/Raphael.Export">

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked">
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global">
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

<ul id="user-links">
  <li>
    <a href="/taejoon" class="name">
      <img alt="Taejoon Kwon" data-user="193309" height="20" src="https://avatars1.githubusercontent.com/u/193309?v=2&amp;s=40" width="20" /> taejoon
    </a>
  </li>

  <li class="new-menu dropdown-toggle js-menu-container">
    <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-arrow"></span>
    </a>

    <div class="new-menu-content js-menu-content">
    </div>
  </li>

  <li>
    <a href="/settings/profile" id="account_settings"
      class="tooltipped tooltipped-s"
      aria-label="Account settings ">
      <span class="octicon octicon-tools"></span>
    </a>
  </li>
  <li>
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="byIgHnChr8K614f1cBQPSTrNdnpMt3chzFxny48TFvbbW7wVIx+2MNe4hTnVkyrNXqR4+pYuSe5hxMWE+9nVdw==" /></div>
      <button class="sign-out-button tooltipped tooltipped-s" aria-label="Sign out">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="https://porter.github.com/new"><span class="octicon octicon-move-right"></span> Import repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="ElbertF/Raphael.Export">This repository</span>
    </li>
      <li>
        <a href="/ElbertF/Raphael.Export/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="iO4ZHbUvz/QGU9BF++7ODwARZObJJBpQ7S9SrtY0pMoQr+zAbqBpFDy4ffTGu32c4G+7Jil4h7ULZXumu8cP/A==" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="2807167" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/ElbertF/Raphael.Export/watchers">
        12
      </a>
      <a href="/ElbertF/Raphael.Export/subscription"
        class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye"></span>
          Watch
        </span>
      </a>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
            <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">Be notified when participating or @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">Be notified of all conversations.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">Never be notified.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
    

  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/ElbertF/Raphael.Export/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="XrewO3p+nSa9TmiB7OOawzy7a7eeDBYBvtXr31v81r4Sa4QaDZXRjqeOHPgWDCoxkQIA6CDxoOi7GlKj0GFofw==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Unstar this repository" title="Unstar ElbertF/Raphael.Export">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/ElbertF/Raphael.Export/stargazers">
          105
        </a>
</form>
    <form accept-charset="UTF-8" action="/ElbertF/Raphael.Export/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="tZdaT+l7u0kwMzUfwwcuIR9SPb8/PihnLqKTBRDk4iGMNupywGz8BDYbOhMut6LRnEuuIJSAKacc9jRzIspQog==" /></div>
      <button
        class="minibutton with-count js-toggler-target star-button"
        aria-label="Star this repository" title="Star ElbertF/Raphael.Export">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/ElbertF/Raphael.Export/stargazers">
          105
        </a>
</form>  </div>

  </li>


        <li>
          <a href="/ElbertF/Raphael.Export/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork your own copy of ElbertF/Raphael.Export to your account" aria-label="Fork your own copy of ElbertF/Raphael.Export to your account" rel="facebox nofollow">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/ElbertF/Raphael.Export/network" class="social-count">30</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/ElbertF" class="url fn" itemprop="url" rel="author"><span itemprop="title">ElbertF</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/ElbertF/Raphael.Export" class="js-current-repository js-repo-home-link">Raphael.Export</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders" data-issue-count-url="/ElbertF/Raphael.Export/issues/counts">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/ElbertF/Raphael.Export" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /ElbertF/Raphael.Export">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/ElbertF/Raphael.Export/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /ElbertF/Raphael.Export/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class="js-issue-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/ElbertF/Raphael.Export/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /ElbertF/Raphael.Export/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class="js-pull-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/ElbertF/Raphael.Export/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g w" data-selected-links="repo_wiki /ElbertF/Raphael.Export/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/ElbertF/Raphael.Export/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /ElbertF/Raphael.Export/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/ElbertF/Raphael.Export/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /ElbertF/Raphael.Export/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/ElbertF/Raphael.Export.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/ElbertF/Raphael.Export.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="git@github.com:ElbertF/Raphael.Export.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="git@github.com:ElbertF/Raphael.Export.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/ElbertF/Raphael.Export" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/ElbertF/Raphael.Export" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/ElbertF/Raphael.Export/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download ElbertF/Raphael.Export as a zip file"
                   title="Download ElbertF/Raphael.Export as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/ElbertF/Raphael.Export/blob/db24084a31ccc884761e19b1c50fff118edf5083/raphael.export.js" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:1baaf48660da2d1faa4093f6c4ec31c4 -->

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/ElbertF/Raphael.Export/blob/master/raphael.export.js"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/ElbertF/Raphael.Export/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="raphael.export.js"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/ElbertF/Raphael.Export" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Raphael.Export</span></a></span></span><span class="separator"> / </span><strong class="final-path">raphael.export.js</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="lumiru" class="main-avatar" data-user="4085705" height="24" src="https://avatars3.githubusercontent.com/u/4085705?v=1&amp;s=48" width="24" />
      <span class="author"><a href="/lumiru" rel="contributor">lumiru</a></span>
      <time datetime="2014-06-04T14:34:27+02:00" is="relative-time">June 04, 2014</time>
      <div class="commit-title">
          <a href="/ElbertF/Raphael.Export/commit/f6bcf8d66cdc47cbd86e66bad4028aa5106191e2" class="message" data-pjax="true" title="IE8 BUGFIX

class is a reserved word in IE.">IE8 BUGFIX</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>8</strong>  contributors</a></p>
          <a class="avatar tooltipped tooltipped-s" aria-label="ElbertF" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=ElbertF"><img alt="Elbert Alias" data-user="77259" height="20" src="https://avatars2.githubusercontent.com/u/77259?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="jtse" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=jtse"><img alt="Jim Tse" data-user="431810" height="20" src="https://avatars0.githubusercontent.com/u/431810?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="tylerault" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=tylerault"><img alt="Tyler Ault" data-user="2236289" height="20" src="https://avatars0.githubusercontent.com/u/2236289?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="bergi9" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=bergi9"><img alt="bergi9" data-user="5556750" height="20" src="https://avatars0.githubusercontent.com/u/5556750?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="dhardtke" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=dhardtke"><img alt="Dominik Hardtke" data-user="1360135" height="20" src="https://avatars0.githubusercontent.com/u/1360135?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="istvan-antal" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=istvan-antal"><img alt="István Miklós Antal" data-user="490764" height="20" src="https://avatars2.githubusercontent.com/u/490764?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="samanbarghi" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=samanbarghi"><img alt="Saman Barghi" data-user="1661187" height="20" src="https://avatars3.githubusercontent.com/u/1661187?v=1&amp;s=40" width="20" /></a>
    <a class="avatar tooltipped tooltipped-s" aria-label="lumiru" href="/ElbertF/Raphael.Export/commits/master/raphael.export.js?author=lumiru"><img alt="lumiru" data-user="4085705" height="20" src="https://avatars1.githubusercontent.com/u/4085705?v=1&amp;s=40" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Elbert Alias" data-user="77259" height="24" src="https://avatars0.githubusercontent.com/u/77259?v=1&amp;s=48" width="24" />
            <a href="/ElbertF">ElbertF</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Jim Tse" data-user="431810" height="24" src="https://avatars2.githubusercontent.com/u/431810?v=1&amp;s=48" width="24" />
            <a href="/jtse">jtse</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Tyler Ault" data-user="2236289" height="24" src="https://avatars2.githubusercontent.com/u/2236289?v=1&amp;s=48" width="24" />
            <a href="/tylerault">tylerault</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="bergi9" data-user="5556750" height="24" src="https://avatars2.githubusercontent.com/u/5556750?v=1&amp;s=48" width="24" />
            <a href="/bergi9">bergi9</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Dominik Hardtke" data-user="1360135" height="24" src="https://avatars2.githubusercontent.com/u/1360135?v=1&amp;s=48" width="24" />
            <a href="/dhardtke">dhardtke</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="István Miklós Antal" data-user="490764" height="24" src="https://avatars0.githubusercontent.com/u/490764?v=1&amp;s=48" width="24" />
            <a href="/istvan-antal">istvan-antal</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="Saman Barghi" data-user="1661187" height="24" src="https://avatars1.githubusercontent.com/u/1661187?v=1&amp;s=48" width="24" />
            <a href="/samanbarghi">samanbarghi</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="lumiru" data-user="4085705" height="24" src="https://avatars3.githubusercontent.com/u/4085705?v=1&amp;s=48" width="24" />
            <a href="/lumiru">lumiru</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>424 lines (362 sloc)</span>
          <span class="meta-divider"></span>
        <span>11.793 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/ElbertF/Raphael.Export/raw/master/raphael.export.js" class="minibutton " id="raw-url">Raw</a>
            <a href="/ElbertF/Raphael.Export/blame/master/raphael.export.js" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/ElbertF/Raphael.Export/commits/master/raphael.export.js" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->


              <a class="octicon-button tooltipped tooltipped-n js-update-url-with-hash"
                 aria-label="Clicking this button will fork this project so you can edit the file"
                 href="/ElbertF/Raphael.Export/edit/master/raphael.export.js"
                 data-method="post" rel="nofollow"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger tooltipped tooltipped-s"
               href="/ElbertF/Raphael.Export/delete/master/raphael.export.js"
               aria-label="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-javascript">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="cm">/**</span></div><div class='line' id='LC2'><span class="cm"> * Raphael.Export https://github.com/ElbertF/Raphael.Export</span></div><div class='line' id='LC3'><span class="cm"> *</span></div><div class='line' id='LC4'><span class="cm"> * Licensed under the MIT license:</span></div><div class='line' id='LC5'><span class="cm"> * http://www.opensource.org/licenses/mit-license.php</span></div><div class='line' id='LC6'><span class="cm"> *</span></div><div class='line' id='LC7'><span class="cm"> */</span></div><div class='line' id='LC8'><br></div><div class='line' id='LC9'><span class="p">(</span><span class="kd">function</span><span class="p">(</span><span class="nx">R</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC10'>	<span class="cm">/**</span></div><div class='line' id='LC11'><span class="cm">	* Escapes string for XML interpolation</span></div><div class='line' id='LC12'><span class="cm">	* @param value string or number value to escape</span></div><div class='line' id='LC13'><span class="cm">	* @returns string escaped</span></div><div class='line' id='LC14'><span class="cm">	*/</span></div><div class='line' id='LC15'>	<span class="kd">function</span> <span class="nx">escapeXML</span><span class="p">(</span><span class="nx">s</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC16'>		<span class="k">if</span> <span class="p">(</span> <span class="k">typeof</span> <span class="nx">s</span> <span class="o">===</span> <span class="s1">&#39;number&#39;</span> <span class="p">)</span> <span class="k">return</span> <span class="nx">s</span><span class="p">.</span><span class="nx">toString</span><span class="p">();</span></div><div class='line' id='LC17'><br></div><div class='line' id='LC18'>		<span class="kd">var</span> <span class="nx">replace</span> <span class="o">=</span> <span class="p">{</span> <span class="s1">&#39;&lt;&#39;</span><span class="o">:</span> <span class="s1">&#39;lt&#39;</span><span class="p">,</span> <span class="s1">&#39;&gt;&#39;</span><span class="o">:</span> <span class="s1">&#39;gt&#39;</span><span class="p">,</span> <span class="s1">&#39;&quot;&#39;</span><span class="o">:</span> <span class="s1">&#39;quot&#39;</span><span class="p">,</span> <span class="s1">&#39;\&#39;&#39;</span><span class="o">:</span> <span class="s1">&#39;apos&#39;</span> <span class="p">};</span></div><div class='line' id='LC19'><br></div><div class='line' id='LC20'>		<span class="k">for</span> <span class="p">(</span> <span class="kd">var</span> <span class="nx">entity</span> <span class="k">in</span> <span class="nx">replace</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC21'>			<span class="nx">s</span> <span class="o">=</span> <span class="nx">s</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="k">new</span> <span class="nb">RegExp</span><span class="p">(</span><span class="nx">entity</span><span class="p">,</span> <span class="s1">&#39;g&#39;</span><span class="p">),</span> <span class="s1">&#39;&amp;&#39;</span> <span class="o">+</span> <span class="nx">replace</span><span class="p">[</span><span class="nx">entity</span><span class="p">]</span> <span class="o">+</span> <span class="s1">&#39;;&#39;</span><span class="p">);</span></div><div class='line' id='LC22'>		<span class="p">}</span></div><div class='line' id='LC23'><br></div><div class='line' id='LC24'>		<span class="k">return</span> <span class="nx">s</span><span class="p">;</span></div><div class='line' id='LC25'>	<span class="p">}</span></div><div class='line' id='LC26'><br></div><div class='line' id='LC27'>	<span class="cm">/**</span></div><div class='line' id='LC28'><span class="cm">	* Generic map function</span></div><div class='line' id='LC29'><span class="cm">	* @param iterable the array or object to be mapped</span></div><div class='line' id='LC30'><span class="cm">	* @param callback the callback function(element, key)</span></div><div class='line' id='LC31'><span class="cm">	* @returns array</span></div><div class='line' id='LC32'><span class="cm">	*/</span></div><div class='line' id='LC33'>	<span class="kd">function</span> <span class="nx">map</span><span class="p">(</span><span class="nx">iterable</span><span class="p">,</span> <span class="nx">callback</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC34'>		<span class="kd">var</span> <span class="nx">mapped</span> <span class="o">=</span> <span class="p">[],</span></div><div class='line' id='LC35'>			<span class="nx">undef</span> <span class="o">=</span> <span class="s1">&#39;undefined&#39;</span><span class="p">,</span></div><div class='line' id='LC36'>			<span class="nx">i</span><span class="p">;</span></div><div class='line' id='LC37'><br></div><div class='line' id='LC38'>		<span class="c1">// use an index iteration if we&#39;re dealing with an array</span></div><div class='line' id='LC39'>		<span class="k">if</span><span class="p">(</span> <span class="k">typeof</span> <span class="nx">iterable</span><span class="p">.</span><span class="nx">unshift</span> <span class="o">!=</span> <span class="s1">&#39;undefined&#39;</span><span class="p">){</span></div><div class='line' id='LC40'>			<span class="kd">var</span> <span class="nx">l</span> <span class="o">=</span> <span class="nx">iterable</span><span class="p">.</span><span class="nx">length</span><span class="p">;</span></div><div class='line' id='LC41'>			<span class="k">for</span> <span class="p">(</span> <span class="nx">i</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="nx">i</span> <span class="o">&lt;</span> <span class="nx">l</span><span class="p">;</span> <span class="nx">i</span><span class="o">++</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC42'>				<span class="k">if</span><span class="p">(</span> <span class="k">typeof</span> <span class="nx">iterable</span><span class="p">[</span><span class="nx">i</span><span class="p">]</span> <span class="o">!=</span> <span class="nx">undef</span> <span class="p">){</span></div><div class='line' id='LC43'>					<span class="kd">var</span> <span class="nx">value</span> <span class="o">=</span> <span class="nx">callback</span><span class="p">.</span><span class="nx">call</span><span class="p">(</span><span class="k">this</span><span class="p">,</span> <span class="nx">iterable</span><span class="p">[</span><span class="nx">i</span><span class="p">],</span> <span class="nx">i</span><span class="p">);</span></div><div class='line' id='LC44'>					<span class="k">if</span><span class="p">(</span> <span class="nx">value</span> <span class="o">!==</span> <span class="kc">null</span> <span class="p">)</span> <span class="nx">mapped</span><span class="p">.</span><span class="nx">push</span><span class="p">(</span><span class="nx">value</span><span class="p">);</span></div><div class='line' id='LC45'>				<span class="p">}</span></div><div class='line' id='LC46'>			<span class="p">}</span></div><div class='line' id='LC47'>		<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC48'>			<span class="k">for</span> <span class="p">(</span> <span class="nx">i</span> <span class="k">in</span> <span class="nx">iterable</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC49'>				<span class="k">if</span> <span class="p">(</span> <span class="nx">iterable</span><span class="p">.</span><span class="nx">hasOwnProperty</span><span class="p">(</span><span class="nx">i</span><span class="p">)</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC50'>					<span class="kd">var</span> <span class="nx">value</span> <span class="o">=</span> <span class="nx">callback</span><span class="p">.</span><span class="nx">call</span><span class="p">(</span><span class="k">this</span><span class="p">,</span> <span class="nx">iterable</span><span class="p">[</span><span class="nx">i</span><span class="p">],</span> <span class="nx">i</span><span class="p">);</span></div><div class='line' id='LC51'>					<span class="k">if</span> <span class="p">(</span> <span class="nx">value</span> <span class="o">!==</span> <span class="kc">null</span> <span class="p">)</span> <span class="nx">mapped</span><span class="p">.</span><span class="nx">push</span><span class="p">(</span><span class="nx">value</span><span class="p">);</span></div><div class='line' id='LC52'>				<span class="p">}</span></div><div class='line' id='LC53'>			<span class="p">}</span></div><div class='line' id='LC54'>		<span class="p">}</span></div><div class='line' id='LC55'><br></div><div class='line' id='LC56'>		<span class="k">return</span> <span class="nx">mapped</span><span class="p">;</span></div><div class='line' id='LC57'>	<span class="p">}</span></div><div class='line' id='LC58'><br></div><div class='line' id='LC59'>	<span class="cm">/**</span></div><div class='line' id='LC60'><span class="cm">	* Generic reduce function</span></div><div class='line' id='LC61'><span class="cm">	* @param iterable array or object to be reduced</span></div><div class='line' id='LC62'><span class="cm">	* @param callback the callback function(initial, element, i)</span></div><div class='line' id='LC63'><span class="cm">	* @param initial the initial value</span></div><div class='line' id='LC64'><span class="cm">	* @return the reduced value</span></div><div class='line' id='LC65'><span class="cm">	*/</span></div><div class='line' id='LC66'>	<span class="kd">function</span> <span class="nx">reduce</span><span class="p">(</span><span class="nx">iterable</span><span class="p">,</span> <span class="nx">callback</span><span class="p">,</span> <span class="nx">initial</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC67'>		<span class="k">for</span> <span class="p">(</span> <span class="kd">var</span> <span class="nx">i</span> <span class="k">in</span> <span class="nx">iterable</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC68'>			<span class="k">if</span> <span class="p">(</span> <span class="nx">iterable</span><span class="p">.</span><span class="nx">hasOwnProperty</span><span class="p">(</span><span class="nx">i</span><span class="p">)</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC69'>				<span class="nx">initial</span> <span class="o">=</span> <span class="nx">callback</span><span class="p">.</span><span class="nx">call</span><span class="p">(</span><span class="k">this</span><span class="p">,</span> <span class="nx">initial</span><span class="p">,</span> <span class="nx">iterable</span><span class="p">[</span><span class="nx">i</span><span class="p">],</span> <span class="nx">i</span><span class="p">);</span></div><div class='line' id='LC70'>			<span class="p">}</span></div><div class='line' id='LC71'>		<span class="p">}</span></div><div class='line' id='LC72'><br></div><div class='line' id='LC73'>		<span class="k">return</span> <span class="nx">initial</span><span class="p">;</span></div><div class='line' id='LC74'>	<span class="p">}</span></div><div class='line' id='LC75'><br></div><div class='line' id='LC76'>	<span class="cm">/**</span></div><div class='line' id='LC77'><span class="cm">	* Utility method for creating a tag</span></div><div class='line' id='LC78'><span class="cm">	* @param name the tag name, e.g., &#39;text&#39;</span></div><div class='line' id='LC79'><span class="cm">	* @param attrs the attribute string, e.g., name1=&quot;val1&quot; name2=&quot;val2&quot;</span></div><div class='line' id='LC80'><span class="cm">	* or attribute map, e.g., { name1 : &#39;val1&#39;, name2 : &#39;val2&#39; }</span></div><div class='line' id='LC81'><span class="cm">	* @param content the content string inside the tag</span></div><div class='line' id='LC82'><span class="cm">	* @returns string of the tag</span></div><div class='line' id='LC83'><span class="cm">	*/</span></div><div class='line' id='LC84'>	<span class="kd">function</span> <span class="nx">tag</span><span class="p">(</span><span class="nx">name</span><span class="p">,</span> <span class="nx">attrs</span><span class="p">,</span> <span class="nx">matrix</span><span class="p">,</span> <span class="nx">content</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC85'>		<span class="k">if</span> <span class="p">(</span> <span class="k">typeof</span> <span class="nx">content</span> <span class="o">===</span> <span class="s1">&#39;undefined&#39;</span> <span class="o">||</span> <span class="nx">content</span> <span class="o">===</span> <span class="kc">null</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC86'>			<span class="nx">content</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC87'>		<span class="p">}</span></div><div class='line' id='LC88'><br></div><div class='line' id='LC89'>		<span class="k">if</span> <span class="p">(</span> <span class="k">typeof</span> <span class="nx">attrs</span> <span class="o">===</span> <span class="s1">&#39;object&#39;</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC90'>			<span class="nx">attrs</span> <span class="o">=</span> <span class="nx">map</span><span class="p">(</span><span class="nx">attrs</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">element</span><span class="p">,</span> <span class="nx">name</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC91'>				<span class="k">switch</span> <span class="p">(</span> <span class="nx">name</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC92'>					<span class="k">case</span> <span class="s1">&#39;transform&#39;</span><span class="o">:</span></div><div class='line' id='LC93'>						<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC94'><br></div><div class='line' id='LC95'>					<span class="k">case</span> <span class="s1">&#39;fill&#39;</span><span class="o">:</span></div><div class='line' id='LC96'>						<span class="k">if</span> <span class="p">(</span> <span class="nx">element</span><span class="p">.</span><span class="nx">match</span><span class="p">(</span><span class="sr">/^hsb/</span><span class="p">)</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC97'>							<span class="kd">var</span> <span class="nx">hsb</span> <span class="o">=</span> <span class="nx">element</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^hsb\(|\)$/g</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">).</span><span class="nx">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">);</span></div><div class='line' id='LC98'><br></div><div class='line' id='LC99'>							<span class="k">if</span> <span class="p">(</span> <span class="nx">hsb</span><span class="p">.</span><span class="nx">length</span> <span class="o">===</span> <span class="mi">3</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC100'>								<span class="nx">element</span> <span class="o">=</span> <span class="nx">R</span><span class="p">.</span><span class="nx">hsb2rgb</span><span class="p">(</span><span class="nx">hsb</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="nx">hsb</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="nx">hsb</span><span class="p">[</span><span class="mi">2</span><span class="p">]).</span><span class="nx">toString</span><span class="p">();</span></div><div class='line' id='LC101'>							<span class="p">}</span></div><div class='line' id='LC102'>						<span class="p">}</span></div><div class='line' id='LC103'>				<span class="p">}</span></div><div class='line' id='LC104'><br></div><div class='line' id='LC105'>				<span class="k">return</span> <span class="nx">name</span> <span class="o">+</span> <span class="s1">&#39;=&quot;&#39;</span> <span class="o">+</span> <span class="nx">escapeXML</span><span class="p">(</span><span class="nx">element</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;&quot;&#39;</span><span class="p">;</span></div><div class='line' id='LC106'>			<span class="p">}).</span><span class="nx">join</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">);</span></div><div class='line' id='LC107'>		<span class="p">}</span></div><div class='line' id='LC108'><br></div><div class='line' id='LC109'>		<span class="k">return</span> <span class="s1">&#39;&lt;&#39;</span> <span class="o">+</span> <span class="nx">name</span> <span class="o">+</span> <span class="p">(</span> <span class="nx">matrix</span> <span class="o">?</span> <span class="s1">&#39; transform=&quot;matrix(&#39;</span> <span class="o">+</span> <span class="nx">matrix</span><span class="p">.</span><span class="nx">toString</span><span class="p">().</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^matrix\(|\)$/g</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;)&quot; &#39;</span> <span class="o">:</span> <span class="s1">&#39; &#39;</span> <span class="p">)</span> <span class="o">+</span> <span class="nx">attrs</span> <span class="o">+</span> <span class="s1">&#39;&gt;&#39;</span> <span class="o">+</span>  <span class="nx">content</span> <span class="o">+</span> <span class="s1">&#39;&lt;/&#39;</span> <span class="o">+</span> <span class="nx">name</span> <span class="o">+</span> <span class="s1">&#39;&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC110'>	<span class="p">}</span></div><div class='line' id='LC111'><br></div><div class='line' id='LC112'>	<span class="cm">/**</span></div><div class='line' id='LC113'><span class="cm">	* @return object the style object</span></div><div class='line' id='LC114'><span class="cm">	*/</span></div><div class='line' id='LC115'>	<span class="kd">function</span> <span class="nx">extractStyle</span><span class="p">(</span><span class="nx">node</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC116'>		<span class="k">return</span> <span class="p">{</span></div><div class='line' id='LC117'>			<span class="nx">font</span><span class="o">:</span> <span class="p">{</span></div><div class='line' id='LC118'>				<span class="nx">family</span><span class="o">:</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">font</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^.*?&quot;(\w+)&quot;.*$/</span><span class="p">,</span> <span class="s1">&#39;$1&#39;</span><span class="p">),</span></div><div class='line' id='LC119'>				<span class="nx">size</span><span class="o">:</span>   <span class="k">typeof</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-size&#39;</span><span class="p">]</span> <span class="o">===</span> <span class="s1">&#39;undefined&#39;</span> <span class="o">?</span> <span class="kc">null</span> <span class="o">:</span> <span class="nb">parseInt</span><span class="p">(</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-size&#39;</span><span class="p">]</span> <span class="p">),</span></div><div class='line' id='LC120'>				<span class="nx">style</span><span class="o">:</span> <span class="k">typeof</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-style&#39;</span><span class="p">]</span> <span class="o">===</span> <span class="s1">&#39;undefined&#39;</span> <span class="o">?</span> <span class="kc">null</span> <span class="o">:</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-style&#39;</span><span class="p">],</span></div><div class='line' id='LC121'>				<span class="nx">weight</span><span class="o">:</span> <span class="k">typeof</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-weight&#39;</span><span class="p">]</span> <span class="o">===</span> <span class="s1">&#39;undefined&#39;</span> <span class="o">?</span> <span class="kc">null</span> <span class="o">:</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;font-weight&#39;</span><span class="p">]</span></div><div class='line' id='LC122'>			<span class="p">},</span></div><div class='line' id='LC123'>			<span class="nx">anchor</span><span class="o">:</span> <span class="k">typeof</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;text-anchor&#39;</span><span class="p">]</span> <span class="o">===</span> <span class="s1">&#39;undefined&#39;</span> <span class="o">?</span> <span class="kc">null</span> <span class="o">:</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;text-anchor&#39;</span><span class="p">]</span></div><div class='line' id='LC124'>		<span class="p">};</span></div><div class='line' id='LC125'>	<span class="p">}</span></div><div class='line' id='LC126'><br></div><div class='line' id='LC127'>	<span class="cm">/**</span></div><div class='line' id='LC128'><span class="cm">	* @param style object from style()</span></div><div class='line' id='LC129'><span class="cm">	* @return string</span></div><div class='line' id='LC130'><span class="cm">	*/</span></div><div class='line' id='LC131'>	<span class="kd">function</span> <span class="nx">styleToString</span><span class="p">(</span><span class="nx">style</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC132'>		<span class="c1">// TODO figure out what is &#39;normal&#39;</span></div><div class='line' id='LC133'>		<span class="c1">// Tyler: it refers to the default inherited from CSS. Order of terms here:</span></div><div class='line' id='LC134'>		<span class="c1">// 		  http://www.w3.org/TR/SVG/text.html#FontProperty</span></div><div class='line' id='LC135'>		<span class="kd">var</span> <span class="nx">norm</span> <span class="o">=</span> <span class="s1">&#39;normal&#39;</span><span class="p">,</span></div><div class='line' id='LC136'>			<span class="nx">textAnchor</span> <span class="o">=</span> <span class="s1">&#39;text-anchor: &#39;</span> <span class="o">+</span> <span class="p">(</span> <span class="nx">style</span><span class="p">.</span><span class="nx">anchor</span> <span class="o">||</span> <span class="s1">&#39;middle&#39;</span> <span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;; &#39;</span><span class="p">,</span></div><div class='line' id='LC137'>			<span class="nx">font</span> <span class="o">=</span> <span class="nx">style</span><span class="p">.</span><span class="nx">font</span><span class="p">;</span></div><div class='line' id='LC138'>		<span class="c1">// return &#39;font: normal normal normal 10px/normal &#39; + style.font.family + ( style.font.size === null ? &#39;&#39; : &#39;; font-size: &#39; + style.font.size + &#39;px&#39; );</span></div><div class='line' id='LC139'>		<span class="k">return</span> <span class="nx">textAnchor</span> <span class="o">+</span> <span class="p">[</span> <span class="s1">&#39;font:&#39;</span><span class="p">,</span></div><div class='line' id='LC140'>		         <span class="p">(</span><span class="nx">font</span><span class="p">.</span><span class="nx">style</span> <span class="o">||</span> <span class="nx">norm</span><span class="p">),</span> <span class="c1">// font-style (e.g. italic)</span></div><div class='line' id='LC141'>		         <span class="nx">norm</span><span class="p">,</span> <span class="c1">// font-variant</span></div><div class='line' id='LC142'>		         <span class="p">(</span><span class="nx">font</span><span class="p">.</span><span class="nx">weight</span> <span class="o">||</span> <span class="nx">norm</span><span class="p">),</span> <span class="c1">// font-weight (e.g. bold)</span></div><div class='line' id='LC143'>		         <span class="p">(</span><span class="nx">font</span><span class="p">.</span><span class="nx">size</span> <span class="o">?</span> <span class="nx">font</span><span class="p">.</span><span class="nx">size</span> <span class="o">+</span> <span class="s1">&#39;px&#39;</span> <span class="o">:</span> <span class="s1">&#39;10px&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;/normal&#39;</span><span class="p">,</span> <span class="c1">// font-size/IGNORED line-height!</span></div><div class='line' id='LC144'>		         <span class="nx">font</span><span class="p">.</span><span class="nx">family</span> <span class="p">].</span><span class="nx">join</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">);</span></div><div class='line' id='LC145'>	<span class="p">}</span></div><div class='line' id='LC146'><br></div><div class='line' id='LC147'>	<span class="cm">/**</span></div><div class='line' id='LC148'><span class="cm">	 * repairs the hex color which missed the &#39;#&#39;</span></div><div class='line' id='LC149'><span class="cm">	 * @param any string</span></div><div class='line' id='LC150'><span class="cm">	 * @return hexvalue of rgb</span></div><div class='line' id='LC151'><span class="cm">	 */</span></div><div class='line' id='LC152'>	<span class="kd">function</span> <span class="nx">convertToHexColor</span><span class="p">(</span><span class="nx">value</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC153'><br></div><div class='line' id='LC154'>		<span class="k">if</span><span class="p">(</span><span class="sr">/^[0-9A-F]{6}$/i</span><span class="p">.</span><span class="nx">test</span><span class="p">(</span><span class="nx">value</span><span class="p">)){</span></div><div class='line' id='LC155'>			<span class="nx">value</span> <span class="o">=</span> <span class="s1">&#39;#&#39;</span> <span class="o">+</span> <span class="nx">value</span><span class="p">;</span></div><div class='line' id='LC156'>		<span class="p">}</span></div><div class='line' id='LC157'><br></div><div class='line' id='LC158'>		<span class="k">return</span> <span class="nx">value</span><span class="p">;</span></div><div class='line' id='LC159'>	<span class="p">}</span></div><div class='line' id='LC160'><br></div><div class='line' id='LC161'>	<span class="cm">/**</span></div><div class='line' id='LC162'><span class="cm">	* Computes tspan dy using font size. This formula was empircally determined</span></div><div class='line' id='LC163'><span class="cm">	* using a best-fit line. Works well in both VML and SVG browsers.</span></div><div class='line' id='LC164'><span class="cm">	* @param fontSize number</span></div><div class='line' id='LC165'><span class="cm">	* @return number</span></div><div class='line' id='LC166'><span class="cm">	*/</span></div><div class='line' id='LC167'>	<span class="kd">function</span> <span class="nx">computeTSpanDy</span><span class="p">(</span><span class="nx">fontSize</span><span class="p">,</span> <span class="nx">line</span><span class="p">,</span> <span class="nx">lines</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC168'>		<span class="k">if</span> <span class="p">(</span> <span class="nx">fontSize</span> <span class="o">===</span> <span class="kc">null</span> <span class="p">)</span> <span class="nx">fontSize</span> <span class="o">=</span> <span class="mi">10</span><span class="p">;</span></div><div class='line' id='LC169'><br></div><div class='line' id='LC170'>		<span class="c1">//return fontSize * 4.5 / 13</span></div><div class='line' id='LC171'>		<span class="k">return</span> <span class="nx">fontSize</span> <span class="o">*</span> <span class="mf">4.5</span> <span class="o">/</span> <span class="mi">13</span> <span class="o">*</span> <span class="p">(</span> <span class="nx">line</span> <span class="o">-</span> <span class="p">.</span><span class="mi">2</span> <span class="o">-</span> <span class="nx">lines</span> <span class="o">/</span> <span class="mi">2</span> <span class="p">)</span> <span class="o">*</span> <span class="mf">3.5</span><span class="p">;</span></div><div class='line' id='LC172'>	<span class="p">}</span></div><div class='line' id='LC173'><br></div><div class='line' id='LC174'>	<span class="kd">var</span> <span class="nx">serializer</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC175'>		<span class="s1">&#39;text&#39;</span><span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">node</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC176'>			<span class="kd">var</span> <span class="nx">style</span> <span class="o">=</span> <span class="nx">extractStyle</span><span class="p">(</span><span class="nx">node</span><span class="p">),</span></div><div class='line' id='LC177'>				<span class="nx">tags</span> <span class="o">=</span> <span class="k">new</span> <span class="nb">Array</span><span class="p">,</span></div><div class='line' id='LC178'>				<span class="nx">textLines</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">].</span><span class="nx">toString</span><span class="p">().</span><span class="nx">split</span><span class="p">(</span><span class="s1">&#39;\n&#39;</span><span class="p">),</span></div><div class='line' id='LC179'>				<span class="nx">totalLines</span> <span class="o">=</span> <span class="nx">textLines</span><span class="p">.</span><span class="nx">length</span><span class="p">;</span></div><div class='line' id='LC180'><br></div><div class='line' id='LC181'>			<span class="nx">map</span><span class="p">(</span><span class="nx">textLines</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">text</span><span class="p">,</span> <span class="nx">line</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC182'>				<span class="kd">var</span> <span class="nx">attrs</span> <span class="o">=</span> <span class="nx">reduce</span><span class="p">(</span></div><div class='line' id='LC183'>					<span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">,</span></div><div class='line' id='LC184'>					<span class="kd">function</span><span class="p">(</span><span class="nx">initial</span><span class="p">,</span> <span class="nx">value</span><span class="p">,</span> <span class="nx">name</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC185'>						<span class="k">if</span> <span class="p">(</span> <span class="nx">name</span> <span class="o">!==</span> <span class="s1">&#39;text&#39;</span> <span class="o">&amp;&amp;</span> <span class="nx">name</span> <span class="o">!==</span> <span class="s1">&#39;w&#39;</span> <span class="o">&amp;&amp;</span> <span class="nx">name</span> <span class="o">!==</span> <span class="s1">&#39;h&#39;</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC186'>							<span class="k">if</span> <span class="p">(</span> <span class="nx">name</span> <span class="o">===</span> <span class="s1">&#39;font-size&#39;</span><span class="p">)</span> <span class="nx">value</span> <span class="o">=</span> <span class="nb">parseInt</span><span class="p">(</span><span class="nx">value</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;px&#39;</span><span class="p">;</span></div><div class='line' id='LC187'><br></div><div class='line' id='LC188'>							<span class="k">if</span><span class="p">(</span> <span class="nx">name</span> <span class="o">===</span> <span class="s1">&#39;stroke&#39;</span><span class="p">){</span></div><div class='line' id='LC189'>								<span class="nx">value</span> <span class="o">=</span> <span class="nx">convertToHexColor</span><span class="p">(</span><span class="nx">value</span><span class="p">);</span></div><div class='line' id='LC190'>							<span class="p">}</span></div><div class='line' id='LC191'><br></div><div class='line' id='LC192'>							<span class="nx">initial</span><span class="p">[</span><span class="nx">name</span><span class="p">]</span> <span class="o">=</span> <span class="nx">escapeXML</span><span class="p">(</span><span class="nx">value</span><span class="p">.</span><span class="nx">toString</span><span class="p">());</span></div><div class='line' id='LC193'>						<span class="p">}</span></div><div class='line' id='LC194'><br></div><div class='line' id='LC195'>						<span class="k">return</span> <span class="nx">initial</span><span class="p">;</span></div><div class='line' id='LC196'>					<span class="p">},</span></div><div class='line' id='LC197'>					<span class="p">{</span> <span class="nx">style</span><span class="o">:</span> <span class="nx">styleToString</span><span class="p">(</span><span class="nx">style</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;;&#39;</span> <span class="p">}</span></div><div class='line' id='LC198'>				<span class="p">);</span></div><div class='line' id='LC199'>				<span class="cm">/**</span></div><div class='line' id='LC200'><span class="cm">				 * if text node has a class set, apply it to the attrs object</span></div><div class='line' id='LC201'><span class="cm">				*/</span></div><div class='line' id='LC202'>				<span class="k">if</span> <span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">node</span><span class="p">.</span><span class="nx">className</span><span class="p">.</span><span class="nx">baseVal</span> <span class="o">!=</span> <span class="s2">&quot;&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC203'>					<span class="nx">attrs</span><span class="p">[</span><span class="s2">&quot;class&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">node</span><span class="p">.</span><span class="nx">className</span><span class="p">.</span><span class="nx">baseVal</span><span class="p">;</span></div><div class='line' id='LC204'>				<span class="p">}</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nx">tags</span><span class="p">.</span><span class="nx">push</span><span class="p">(</span><span class="nx">tag</span><span class="p">(</span></div><div class='line' id='LC206'>					<span class="s1">&#39;text&#39;</span><span class="p">,</span></div><div class='line' id='LC207'>					<span class="nx">attrs</span><span class="p">,</span></div><div class='line' id='LC208'>					<span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span><span class="p">,</span></div><div class='line' id='LC209'>					<span class="nx">tag</span><span class="p">(</span><span class="s1">&#39;tspan&#39;</span><span class="p">,</span> <span class="p">{</span> <span class="nx">dy</span><span class="o">:</span> <span class="nx">computeTSpanDy</span><span class="p">(</span><span class="nx">style</span><span class="p">.</span><span class="nx">font</span><span class="p">.</span><span class="nx">size</span><span class="p">,</span> <span class="nx">line</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="nx">totalLines</span><span class="p">)</span> <span class="p">},</span> <span class="kc">null</span><span class="p">,</span> <span class="nx">text</span><span class="p">.</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/&amp;/g</span><span class="p">,</span> <span class="s2">&quot;&amp;amp;&quot;</span><span class="p">))</span></div><div class='line' id='LC210'>				<span class="p">));</span></div><div class='line' id='LC211'>			<span class="p">});</span></div><div class='line' id='LC212'><br></div><div class='line' id='LC213'>			<span class="k">return</span> <span class="nx">tags</span><span class="p">;</span></div><div class='line' id='LC214'>		<span class="p">},</span></div><div class='line' id='LC215'>		<span class="s1">&#39;path&#39;</span> <span class="o">:</span> <span class="kd">function</span><span class="p">(</span><span class="nx">node</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC216'>			<span class="kd">var</span> <span class="nx">initial</span> <span class="o">=</span> <span class="p">(</span> <span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span><span class="p">.</span><span class="nx">a</span> <span class="o">===</span> <span class="mi">1</span> <span class="o">&amp;&amp;</span> <span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span><span class="p">.</span><span class="nx">d</span> <span class="o">===</span> <span class="mi">1</span> <span class="p">)</span> <span class="o">?</span> <span class="p">{}</span> <span class="o">:</span> <span class="p">{</span> <span class="s1">&#39;transform&#39;</span> <span class="o">:</span> <span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span><span class="p">.</span><span class="nx">toString</span><span class="p">()</span> <span class="p">};</span></div><div class='line' id='LC217'><br></div><div class='line' id='LC218'>			<span class="k">return</span> <span class="nx">tag</span><span class="p">(</span></div><div class='line' id='LC219'>				<span class="s1">&#39;path&#39;</span><span class="p">,</span></div><div class='line' id='LC220'>				<span class="nx">reduce</span><span class="p">(</span></div><div class='line' id='LC221'>					<span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">,</span></div><div class='line' id='LC222'>					<span class="kd">function</span><span class="p">(</span><span class="nx">initial</span><span class="p">,</span> <span class="nx">value</span><span class="p">,</span> <span class="nx">name</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC223'>						<span class="k">if</span> <span class="p">(</span> <span class="nx">name</span> <span class="o">===</span> <span class="s1">&#39;path&#39;</span> <span class="p">)</span> <span class="nx">name</span> <span class="o">=</span> <span class="s1">&#39;d&#39;</span><span class="p">;</span></div><div class='line' id='LC224'><br></div><div class='line' id='LC225'>						<span class="k">if</span><span class="p">(</span> <span class="nx">name</span> <span class="o">===</span> <span class="s1">&#39;stroke&#39;</span><span class="p">){</span></div><div class='line' id='LC226'>							<span class="nx">value</span> <span class="o">=</span> <span class="nx">convertToHexColor</span><span class="p">(</span><span class="nx">value</span><span class="p">);</span></div><div class='line' id='LC227'>						<span class="p">}</span></div><div class='line' id='LC228'><br></div><div class='line' id='LC229'>						<span class="nx">initial</span><span class="p">[</span><span class="nx">name</span><span class="p">]</span> <span class="o">=</span> <span class="nx">value</span><span class="p">.</span><span class="nx">toString</span><span class="p">();</span></div><div class='line' id='LC230'><br></div><div class='line' id='LC231'>						<span class="k">return</span> <span class="nx">initial</span><span class="p">;</span></div><div class='line' id='LC232'>					<span class="p">},</span></div><div class='line' id='LC233'>					<span class="p">{}</span></div><div class='line' id='LC234'>				<span class="p">),</span></div><div class='line' id='LC235'>				<span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span></div><div class='line' id='LC236'>				<span class="p">);</span></div><div class='line' id='LC237'>		<span class="p">}</span></div><div class='line' id='LC238'>		<span class="c1">// Other serializers should go here</span></div><div class='line' id='LC239'>	<span class="p">};</span></div><div class='line' id='LC240'><br></div><div class='line' id='LC241'>	<span class="nx">R</span><span class="p">.</span><span class="nx">fn</span><span class="p">.</span><span class="nx">toSVG</span> <span class="o">=</span> <span class="kd">function</span><span class="p">()</span> <span class="p">{</span></div><div class='line' id='LC242'>		<span class="kd">var</span></div><div class='line' id='LC243'>			<span class="nx">paper</span>   <span class="o">=</span> <span class="k">this</span><span class="p">,</span></div><div class='line' id='LC244'>			<span class="nx">restore</span> <span class="o">=</span> <span class="p">{</span> <span class="nx">svg</span><span class="o">:</span> <span class="nx">R</span><span class="p">.</span><span class="nx">svg</span><span class="p">,</span> <span class="nx">vml</span><span class="o">:</span> <span class="nx">R</span><span class="p">.</span><span class="nx">vml</span> <span class="p">},</span></div><div class='line' id='LC245'>			<span class="nx">svg</span>     <span class="o">=</span> <span class="s1">&#39;&lt;svg style=&quot;overflow: hidden; position: relative;&quot; xmlns=&quot;http://www.w3.org/2000/svg&quot; xmlns:xlink=&quot;http://www.w3.org/1999/xlink&quot; width=&quot;&#39;</span> <span class="o">+</span> <span class="nx">paper</span><span class="p">.</span><span class="nx">width</span> <span class="o">+</span> <span class="s1">&#39;&quot; version=&quot;1.1&quot; height=&quot;&#39;</span> <span class="o">+</span> <span class="nx">paper</span><span class="p">.</span><span class="nx">height</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&#39;</span></div><div class='line' id='LC246'>			<span class="p">;</span></div><div class='line' id='LC247'><br></div><div class='line' id='LC248'>		<span class="nx">R</span><span class="p">.</span><span class="nx">svg</span> <span class="o">=</span> <span class="kc">true</span><span class="p">;</span></div><div class='line' id='LC249'>		<span class="nx">R</span><span class="p">.</span><span class="nx">vml</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC250'><br></div><div class='line' id='LC251'>		<span class="k">for</span> <span class="p">(</span> <span class="kd">var</span> <span class="nx">node</span> <span class="o">=</span> <span class="nx">paper</span><span class="p">.</span><span class="nx">bottom</span><span class="p">;</span> <span class="nx">node</span> <span class="o">!=</span> <span class="kc">null</span><span class="p">;</span> <span class="nx">node</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">next</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC252'>			<span class="k">if</span> <span class="p">(</span> <span class="nx">node</span><span class="p">.</span><span class="nx">node</span><span class="p">.</span><span class="nx">style</span><span class="p">.</span><span class="nx">display</span> <span class="o">===</span> <span class="s1">&#39;none&#39;</span> <span class="p">)</span> <span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC253'><br></div><div class='line' id='LC254'>			<span class="kd">var</span> <span class="nx">attrs</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC255'><br></div><div class='line' id='LC256'>			<span class="c1">// Use serializer</span></div><div class='line' id='LC257'>			<span class="k">if</span> <span class="p">(</span> <span class="k">typeof</span> <span class="nx">serializer</span><span class="p">[</span><span class="nx">node</span><span class="p">.</span><span class="nx">type</span><span class="p">]</span> <span class="o">===</span> <span class="s1">&#39;function&#39;</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC258'>				<span class="nx">svg</span> <span class="o">+=</span> <span class="nx">serializer</span><span class="p">[</span><span class="nx">node</span><span class="p">.</span><span class="nx">type</span><span class="p">](</span><span class="nx">node</span><span class="p">);</span></div><div class='line' id='LC259'><br></div><div class='line' id='LC260'>				<span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC261'>			<span class="p">}</span></div><div class='line' id='LC262'><br></div><div class='line' id='LC263'>			<span class="k">switch</span> <span class="p">(</span> <span class="nx">node</span><span class="p">.</span><span class="nx">type</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC264'>				<span class="k">case</span> <span class="s1">&#39;image&#39;</span><span class="o">:</span></div><div class='line' id='LC265'>					<span class="nx">attrs</span> <span class="o">+=</span> <span class="s1">&#39; preserveAspectRatio=&quot;none&quot;&#39;</span><span class="p">;</span></div><div class='line' id='LC266'>					<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC267'>			<span class="p">}</span></div><div class='line' id='LC268'><br></div><div class='line' id='LC269'>			<span class="k">for</span> <span class="p">(</span> <span class="nx">i</span> <span class="k">in</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC270'>				<span class="kd">var</span> <span class="nx">name</span> <span class="o">=</span> <span class="nx">i</span><span class="p">;</span></div><div class='line' id='LC271'>				<span class="kd">var</span> <span class="nx">value</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC272'><br></div><div class='line' id='LC273'>				<span class="k">switch</span> <span class="p">(</span> <span class="nx">i</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC274'>					<span class="k">case</span> <span class="s1">&#39;r&#39;</span><span class="o">:</span></div><div class='line' id='LC275'>						<span class="c1">// see https://github.com/ElbertF/Raphael.Export/issues/40</span></div><div class='line' id='LC276'>						<span class="k">if</span> <span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">type</span> <span class="o">!=</span> <span class="s2">&quot;rect&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC277'>							<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC278'>						<span class="p">}</span></div><div class='line' id='LC279'><br></div><div class='line' id='LC280'>						<span class="cm">/**</span></div><div class='line' id='LC281'><span class="cm">						 * set &#39;rx&#39; and &#39;ry&#39; to &#39;r&#39;</span></div><div class='line' id='LC282'><span class="cm">						*/</span></div><div class='line' id='LC283'>						<span class="nx">value</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">r</span><span class="p">;</span></div><div class='line' id='LC284'>						<span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">rx</span> <span class="o">=</span> <span class="nx">value</span><span class="p">;</span></div><div class='line' id='LC285'>						<span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">ry</span> <span class="o">=</span> <span class="nx">value</span><span class="p">;</span></div><div class='line' id='LC286'><br></div><div class='line' id='LC287'>						<span class="cm">/**</span></div><div class='line' id='LC288'><span class="cm">						 * skip adding the &#39;r&#39; attribute</span></div><div class='line' id='LC289'><span class="cm">						*/</span></div><div class='line' id='LC290'>						<span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC291'><br></div><div class='line' id='LC292'>					<span class="k">case</span> <span class="s1">&#39;src&#39;</span><span class="o">:</span></div><div class='line' id='LC293'>						<span class="nx">name</span> <span class="o">=</span> <span class="s1">&#39;xlink:href&#39;</span><span class="p">;</span></div><div class='line' id='LC294'><br></div><div class='line' id='LC295'>						<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC296'>					<span class="k">case</span> <span class="s1">&#39;transform&#39;</span><span class="o">:</span></div><div class='line' id='LC297'>						<span class="nx">name</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC298'><br></div><div class='line' id='LC299'>						<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC300'><br></div><div class='line' id='LC301'>					<span class="k">case</span> <span class="s1">&#39;fill&#39;</span><span class="o">:</span></div><div class='line' id='LC302'>						<span class="c1">//skip if there is any gradient</span></div><div class='line' id='LC303'>						<span class="k">if</span><span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">gradient</span><span class="p">)</span></div><div class='line' id='LC304'>							<span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC305'>						<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC306'>					<span class="k">case</span> <span class="s1">&#39;gradient&#39;</span><span class="o">:</span></div><div class='line' id='LC307'>						<span class="c1">//radial gradient</span></div><div class='line' id='LC308'>						<span class="kd">var</span> <span class="nx">id</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">id</span><span class="p">;</span></div><div class='line' id='LC309'>						<span class="kd">var</span> <span class="nx">gradient</span> <span class="o">=</span> <span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">gradient</span><span class="p">;</span></div><div class='line' id='LC310'>						<span class="kd">var</span> <span class="nx">fx</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nx">fy</span><span class="o">=</span><span class="mf">0.5</span><span class="p">;</span></div><div class='line' id='LC311'>						<span class="nx">gradient</span> <span class="o">=</span> <span class="nb">String</span><span class="p">(</span><span class="nx">gradient</span><span class="p">).</span><span class="nx">replace</span><span class="p">(</span><span class="nx">R</span><span class="p">.</span><span class="nx">_radial_gradient</span><span class="p">,</span> <span class="kd">function</span> <span class="p">(</span><span class="nx">all</span><span class="p">,</span> <span class="nx">_fx</span><span class="p">,</span> <span class="nx">_fy</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC312'>			                <span class="nx">type</span> <span class="o">=</span> <span class="s2">&quot;radial&quot;</span><span class="p">;</span></div><div class='line' id='LC313'>			                <span class="k">if</span> <span class="p">(</span><span class="nx">_fx</span> <span class="o">&amp;&amp;</span> <span class="nx">_fy</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC314'>			                    <span class="nx">fx</span> <span class="o">=</span> <span class="nb">parseFloat</span><span class="p">(</span><span class="nx">_fx</span><span class="p">);</span></div><div class='line' id='LC315'>			                    <span class="nx">fy</span> <span class="o">=</span> <span class="nb">parseFloat</span><span class="p">(</span><span class="nx">_fy</span><span class="p">);</span></div><div class='line' id='LC316'>			                    <span class="kd">var</span> <span class="nx">dir</span> <span class="o">=</span> <span class="p">((</span><span class="nx">fy</span> <span class="o">&gt;</span> <span class="p">.</span><span class="mi">5</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">-</span> <span class="mi">1</span><span class="p">);</span></div><div class='line' id='LC317'>			                    <span class="nb">Math</span><span class="p">.</span><span class="nx">pow</span><span class="p">(</span><span class="nx">fx</span> <span class="o">-</span> <span class="p">.</span><span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">+</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">pow</span><span class="p">(</span><span class="nx">fy</span> <span class="o">-</span> <span class="p">.</span><span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">&gt;</span> <span class="p">.</span><span class="mi">25</span> <span class="o">&amp;&amp;</span></div><div class='line' id='LC318'>			                        <span class="p">(</span><span class="nx">fy</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">sqrt</span><span class="p">(.</span><span class="mi">25</span> <span class="o">-</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">pow</span><span class="p">(</span><span class="nx">fx</span> <span class="o">-</span> <span class="p">.</span><span class="mi">5</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span> <span class="o">*</span> <span class="nx">dir</span> <span class="o">+</span> <span class="p">.</span><span class="mi">5</span><span class="p">)</span> <span class="o">&amp;&amp;</span></div><div class='line' id='LC319'>			                        <span class="nx">fy</span> <span class="o">!=</span> <span class="p">.</span><span class="mi">5</span> <span class="o">&amp;&amp;</span></div><div class='line' id='LC320'>			                        <span class="p">(</span><span class="nx">fy</span> <span class="o">=</span> <span class="nx">fy</span><span class="p">.</span><span class="nx">toFixed</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span><span class="nx">e</span><span class="o">-</span><span class="mi">5</span> <span class="o">*</span> <span class="nx">dir</span><span class="p">);</span></div><div class='line' id='LC321'>			                <span class="p">}</span></div><div class='line' id='LC322'>			                <span class="k">return</span> <span class="s1">&#39;&#39;</span><span class="p">;</span></div><div class='line' id='LC323'>			            <span class="p">});</span></div><div class='line' id='LC324'>						<span class="nx">gradient</span> <span class="o">=</span> <span class="nx">gradient</span><span class="p">.</span><span class="nx">split</span><span class="p">(</span><span class="sr">/\s*\-\s*/</span><span class="p">);</span></div><div class='line' id='LC325'>						<span class="k">if</span><span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">.</span><span class="nx">gradient</span><span class="p">.</span><span class="nx">match</span><span class="p">(</span><span class="sr">/^r/g</span><span class="p">)){</span></div><div class='line' id='LC326'>							<span class="kd">var</span> <span class="nx">dots</span> <span class="o">=</span> <span class="nx">R</span><span class="p">.</span><span class="nx">_parseDots</span><span class="p">(</span><span class="nx">gradient</span><span class="p">);</span></div><div class='line' id='LC327'>							<span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="nx">dots</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC328'>				                <span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC329'>				            <span class="p">}</span>	</div><div class='line' id='LC330'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;defs&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC331'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;	    &lt;radialGradient id=&quot;radialgradient&#39;</span><span class="o">+</span><span class="nx">id</span><span class="o">+</span><span class="s1">&#39;&quot; fx=&quot;&#39;</span><span class="o">+</span><span class="nx">fx</span><span class="o">+</span><span class="s1">&#39;&quot; fy=&quot;&#39;</span><span class="o">+</span><span class="nx">fy</span><span class="o">+</span><span class="s1">&#39;&quot; &gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC332'><br></div><div class='line' id='LC333'>							<span class="k">for</span><span class="p">(</span><span class="kd">var</span> <span class="nx">di</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="nx">di</span> <span class="o">&lt;</span> <span class="nx">dots</span><span class="p">.</span><span class="nx">length</span><span class="p">;</span> <span class="nx">di</span><span class="o">++</span><span class="p">){</span></div><div class='line' id='LC334'>								<span class="kd">var</span> <span class="nx">offset</span> <span class="o">=</span> <span class="p">(</span><span class="nx">di</span><span class="o">/</span><span class="p">(</span><span class="nx">dots</span><span class="p">.</span><span class="nx">length</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">+</span><span class="s1">&#39;%&#39;</span><span class="p">;</span></div><div class='line' id='LC335'>								<span class="c1">//if dot has an offset</span></div><div class='line' id='LC336'>								<span class="k">if</span><span class="p">(</span><span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">offset</span><span class="p">)</span>							</div><div class='line' id='LC337'>									<span class="nx">offset</span> <span class="o">=</span> <span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">offset</span><span class="p">;</span></div><div class='line' id='LC338'>								<span class="nx">svg</span> <span class="o">+=</span>  <span class="s1">&#39;&lt;stop stop-color=&quot;&#39;</span><span class="o">+</span><span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">color</span><span class="o">+</span><span class="s1">&#39;&quot; offset=&quot;&#39;</span><span class="o">+</span><span class="nx">offset</span><span class="o">+</span><span class="s1">&#39;&quot;/&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC339'>							<span class="p">}</span></div><div class='line' id='LC340'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;    &lt;/radialGradient&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC341'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;/defs&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC342'><br></div><div class='line' id='LC343'>							<span class="nx">name</span> <span class="o">=</span> <span class="s1">&#39;fill&#39;</span><span class="p">;</span></div><div class='line' id='LC344'>							<span class="nx">value</span> <span class="o">=</span> <span class="s1">&#39;url(#radialgradient&#39;</span><span class="o">+</span><span class="nx">id</span><span class="o">+</span><span class="s1">&#39;)&#39;</span><span class="p">;</span></div><div class='line' id='LC345'><br></div><div class='line' id='LC346'>						<span class="p">}</span><span class="k">else</span><span class="p">{</span><span class="c1">//linear gradient</span></div><div class='line' id='LC347'><br></div><div class='line' id='LC348'>							<span class="c1">//assuming gradient is validated already!!</span></div><div class='line' id='LC349'>							<span class="kd">var</span> <span class="nx">angle</span> <span class="o">=</span> <span class="nx">gradient</span><span class="p">.</span><span class="nx">shift</span><span class="p">();</span></div><div class='line' id='LC350'>							<span class="nx">angle</span> <span class="o">=</span> <span class="nb">parseFloat</span><span class="p">(</span><span class="nx">angle</span><span class="p">)</span><span class="o">*-</span><span class="mi">1</span><span class="p">;</span></div><div class='line' id='LC351'>			                <span class="k">if</span> <span class="p">(</span><span class="nb">isNaN</span><span class="p">(</span><span class="nx">angle</span><span class="p">))</span> <span class="p">{</span></div><div class='line' id='LC352'>			                   <span class="k">continue</span><span class="p">;</span> </div><div class='line' id='LC353'>			                <span class="p">}</span></div><div class='line' id='LC354'>							<span class="kd">var</span> <span class="nx">dots</span> <span class="o">=</span> <span class="nx">R</span><span class="p">.</span><span class="nx">_parseDots</span><span class="p">(</span><span class="nx">gradient</span><span class="p">);</span></div><div class='line' id='LC355'>							<span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="nx">dots</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC356'>				                <span class="k">continue</span><span class="p">;</span></div><div class='line' id='LC357'>				            <span class="p">}</span></div><div class='line' id='LC358'>				            <span class="kd">var</span> <span class="nx">vector</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">cos</span><span class="p">(</span><span class="nx">R</span><span class="p">.</span><span class="nx">rad</span><span class="p">(</span><span class="nx">angle</span><span class="p">)),</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">sin</span><span class="p">(</span><span class="nx">R</span><span class="p">.</span><span class="nx">rad</span><span class="p">(</span><span class="nx">angle</span><span class="p">))],</span></div><div class='line' id='LC359'>			                       <span class="nx">max</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span> <span class="p">(</span><span class="nb">Math</span><span class="p">.</span><span class="nx">max</span><span class="p">(</span><span class="nb">Math</span><span class="p">.</span><span class="nx">abs</span><span class="p">(</span><span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">]),</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">abs</span><span class="p">(</span><span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">]))</span> <span class="o">||</span> <span class="mi">1</span><span class="p">);</span></div><div class='line' id='LC360'>			                <span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">*=</span> <span class="nx">max</span><span class="p">;</span></div><div class='line' id='LC361'>			                <span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">*=</span> <span class="nx">max</span><span class="p">;</span></div><div class='line' id='LC362'>			                <span class="k">if</span> <span class="p">(</span><span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC363'>			                    <span class="nx">vector</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">];</span></div><div class='line' id='LC364'>			                    <span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC365'>			                <span class="p">}</span></div><div class='line' id='LC366'>			                <span class="k">if</span> <span class="p">(</span><span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC367'>			                    <span class="nx">vector</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">];</span></div><div class='line' id='LC368'>			                    <span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC369'>			                <span class="p">}</span></div><div class='line' id='LC370'><br></div><div class='line' id='LC371'>				            <span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;defs&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC372'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;	    &lt;linearGradient id=&quot;lineargradient&#39;</span><span class="o">+</span><span class="nx">id</span><span class="o">+</span><span class="s1">&#39;&quot; x1=&quot;&#39;</span><span class="o">+</span><span class="nx">vector</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">+</span><span class="s1">&#39;&quot; y1=&quot;&#39;</span><span class="o">+</span><span class="nx">vector</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">+</span><span class="s1">&#39;&quot; x2=&quot;&#39;</span><span class="o">+</span><span class="nx">vector</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">+</span><span class="s1">&#39;&quot; y2=&quot;&#39;</span><span class="o">+</span><span class="nx">vector</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">+</span><span class="s1">&#39;&quot;&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC373'><br></div><div class='line' id='LC374'>							<span class="k">for</span><span class="p">(</span><span class="kd">var</span> <span class="nx">di</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span> <span class="nx">di</span> <span class="o">&lt;</span> <span class="nx">dots</span><span class="p">.</span><span class="nx">length</span><span class="p">;</span> <span class="nx">di</span><span class="o">++</span><span class="p">){</span></div><div class='line' id='LC375'>								<span class="kd">var</span> <span class="nx">offset</span> <span class="o">=</span> <span class="p">(</span><span class="nx">di</span><span class="o">/</span><span class="p">(</span><span class="nx">dots</span><span class="p">.</span><span class="nx">length</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="mi">100</span><span class="p">)</span><span class="o">+</span><span class="s1">&#39;%&#39;</span><span class="p">;</span></div><div class='line' id='LC376'>								<span class="c1">//if dot has an offset</span></div><div class='line' id='LC377'>								<span class="k">if</span><span class="p">(</span><span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">offset</span><span class="p">)</span>							</div><div class='line' id='LC378'>									<span class="nx">offset</span> <span class="o">=</span> <span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">offset</span><span class="p">;</span></div><div class='line' id='LC379'>								<span class="nx">svg</span> <span class="o">+=</span>  <span class="s1">&#39;&lt;stop stop-color=&quot;&#39;</span><span class="o">+</span><span class="nx">dots</span><span class="p">[</span><span class="nx">di</span><span class="p">].</span><span class="nx">color</span><span class="o">+</span><span class="s1">&#39;&quot; offset=&quot;&#39;</span><span class="o">+</span><span class="nx">offset</span><span class="o">+</span><span class="s1">&#39;&quot;/&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC380'>							<span class="p">}</span></div><div class='line' id='LC381'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;    &lt;/linearGradient&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC382'>							<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;/defs&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC383'><br></div><div class='line' id='LC384'>							<span class="nx">name</span> <span class="o">=</span> <span class="s1">&#39;fill&#39;</span><span class="p">;</span></div><div class='line' id='LC385'>							<span class="nx">value</span> <span class="o">=</span> <span class="s1">&#39;url(#lineargradient&#39;</span><span class="o">+</span><span class="nx">id</span><span class="o">+</span><span class="s1">&#39;)&#39;</span><span class="p">;</span></div><div class='line' id='LC386'><br></div><div class='line' id='LC387'>						<span class="p">}</span></div><div class='line' id='LC388'>						<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC389'>					<span class="k">case</span> <span class="s1">&#39;stroke&#39;</span><span class="o">:</span></div><div class='line' id='LC390'>						<span class="k">if</span><span class="p">(</span><span class="nx">value</span><span class="p">){</span></div><div class='line' id='LC391'>							<span class="nx">value</span> <span class="o">=</span> <span class="nx">convertToHexColor</span><span class="p">(</span><span class="nx">value</span><span class="p">);</span></div><div class='line' id='LC392'>						<span class="p">}</span><span class="k">else</span><span class="p">{</span></div><div class='line' id='LC393'>							<span class="nx">value</span> <span class="o">=</span> <span class="nx">convertToHexColor</span><span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">toString</span><span class="p">());</span></div><div class='line' id='LC394'>						<span class="p">}</span></div><div class='line' id='LC395'>						<span class="k">break</span><span class="p">;</span></div><div class='line' id='LC396'>				<span class="p">}</span></div><div class='line' id='LC397'><br></div><div class='line' id='LC398'>				<span class="k">if</span> <span class="p">(</span> <span class="nx">name</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC399'>					<span class="k">if</span><span class="p">(</span><span class="nx">value</span><span class="p">)</span></div><div class='line' id='LC400'>						<span class="nx">attrs</span> <span class="o">+=</span> <span class="s1">&#39; &#39;</span> <span class="o">+</span> <span class="nx">name</span> <span class="o">+</span> <span class="s1">&#39;=&quot;&#39;</span> <span class="o">+</span> <span class="nx">escapeXML</span><span class="p">(</span><span class="nx">value</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;&quot;&#39;</span><span class="p">;</span></div><div class='line' id='LC401'>					<span class="k">else</span></div><div class='line' id='LC402'>						<span class="nx">attrs</span> <span class="o">+=</span> <span class="s1">&#39; &#39;</span> <span class="o">+</span> <span class="nx">name</span> <span class="o">+</span> <span class="s1">&#39;=&quot;&#39;</span> <span class="o">+</span> <span class="nx">escapeXML</span><span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">attrs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">toString</span><span class="p">())</span> <span class="o">+</span> <span class="s1">&#39;&quot;&#39;</span><span class="p">;</span></div><div class='line' id='LC403'>				<span class="p">}</span></div><div class='line' id='LC404'>			<span class="p">}</span></div><div class='line' id='LC405'><br></div><div class='line' id='LC406'>			<span class="cm">/**</span></div><div class='line' id='LC407'><span class="cm">			 * if node has a class set, append it to the attrs string</span></div><div class='line' id='LC408'><span class="cm">		    */</span></div><div class='line' id='LC409'>			<span class="k">if</span> <span class="p">(</span><span class="nx">node</span><span class="p">.</span><span class="nx">node</span><span class="p">.</span><span class="nx">className</span><span class="p">.</span><span class="nx">baseVal</span> <span class="o">!=</span> <span class="s2">&quot;&quot;</span><span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC410'>				<span class="nx">attrs</span> <span class="o">+=</span> <span class="s1">&#39; &#39;</span> <span class="o">+</span> <span class="s1">&#39;class=&quot;&#39;</span> <span class="o">+</span> <span class="nx">node</span><span class="p">.</span><span class="nx">node</span><span class="p">.</span><span class="nx">className</span><span class="p">.</span><span class="nx">baseVal</span> <span class="o">+</span> <span class="s1">&#39;&quot;&#39;</span><span class="p">;</span></div><div class='line' id='LC411'>			<span class="p">}</span></div><div class='line' id='LC412'><br></div><div class='line' id='LC413'>			<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;&#39;</span> <span class="o">+</span> <span class="nx">node</span><span class="p">.</span><span class="nx">type</span> <span class="o">+</span> <span class="s1">&#39; transform=&quot;matrix(&#39;</span> <span class="o">+</span> <span class="nx">node</span><span class="p">.</span><span class="nx">matrix</span><span class="p">.</span><span class="nx">toString</span><span class="p">().</span><span class="nx">replace</span><span class="p">(</span><span class="sr">/^matrix\(|\)$/g</span><span class="p">,</span> <span class="s1">&#39;&#39;</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39;)&quot;&#39;</span> <span class="o">+</span> <span class="nx">attrs</span> <span class="o">+</span> <span class="s1">&#39;&gt;&lt;/&#39;</span> <span class="o">+</span> <span class="nx">node</span><span class="p">.</span><span class="nx">type</span> <span class="o">+</span> <span class="s1">&#39;&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC414'>		<span class="p">}</span></div><div class='line' id='LC415'><br></div><div class='line' id='LC416'>		<span class="nx">svg</span> <span class="o">+=</span> <span class="s1">&#39;&lt;/svg&gt;&#39;</span><span class="p">;</span></div><div class='line' id='LC417'><br></div><div class='line' id='LC418'>		<span class="nx">R</span><span class="p">.</span><span class="nx">svg</span> <span class="o">=</span> <span class="nx">restore</span><span class="p">.</span><span class="nx">svg</span><span class="p">;</span></div><div class='line' id='LC419'>		<span class="nx">R</span><span class="p">.</span><span class="nx">vml</span> <span class="o">=</span> <span class="nx">restore</span><span class="p">.</span><span class="nx">vml</span><span class="p">;</span></div><div class='line' id='LC420'><br></div><div class='line' id='LC421'>		<span class="k">return</span> <span class="nx">svg</span><span class="p">;</span></div><div class='line' id='LC422'>	<span class="p">};</span></div><div class='line' id='LC423'><span class="p">})(</span><span class="nb">window</span><span class="p">.</span><span class="nx">Raphael</span><span class="p">);</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.04697s from github-fe120-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-12d5fda141e78e513749dddbc56445fe172cbd9a.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-beb666a0d7747890d0c108e446adea3009066037.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

