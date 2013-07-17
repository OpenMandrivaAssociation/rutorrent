Summary:	Web frontend for the rTorrent bittorrent client
Name:		rutorrent
Version:	3.2
Release:	4
License:	GPLv3
Group:		Networking/File transfer
URL:		http://code.google.com/p/rutorrent/
Source:		http://rutorrent.googlecode.com/files/%{name}-%{version}.tar.gz
# Plugins are here in the same .spec for simplicity as they mostly share
# rutorrent's version number. If this changes in the future or it is otherwise
# seemed better, this can be splitted to one or more separate src.rpms.
# - Anssi 08/2010
Source1:	http://rutorrent.googlecode.com/files/plugins-%{version}.tar.gz
Patch0:		rutorrent-fhs.patch
Patch1:		rutorrent-log.patch
# Load a "backup" config file before the actual config file.
# In case of an unhandled .rpmnew file, the possible newly added configuration
# options are loaded from the backup file. This is similar in how e.g. normal
# initscript configurations are handled. - Anssi 08/2010
Patch2:		rutorrent-defaults.patch
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch
Requires:	webserver
# suggests to allow other webservers:
Suggests:	apache-mod_php
# for apache user:
Requires(pre):	apache-conf

%description
rutorrent is a web frontend for the rTorrent bittorrent client.

Plugin packages are named rutorrent-plugin-*.

Note that you need to either configure an SCGI module for your web server or
install rutorrent-plugin-rpc or rutorrent-plugin-httprpc for rutorrent to
work. See the online documentation for more details.
All configuration files, including plugin configuration, are in
%{_sysconfdir}/%{name}.

# mkplugin(plugin_name, version, url)
%define mkplugin() \
%package plugin-%{1} \
Summary:	rutorrent plugin: %{expand:%{%{1}_summary}} \
Requires:	%{name} = %{version} \
%{expand:%%{?%{1}_req:Requires: %{%{1}_req}}} \
Group:		Networking/File transfer \
%description plugin-%{1} \
%(echo "%{expand:%{%{1}_desc}}" | fold -s) \
\
This is a plugin for rutorrent, a web frontend for the rTorrent bittorrent \
client. \
%files plugin-%{1} -f lists/%{1}.list \
%defattr(-,root,root) \
%{_datadir}/%{name}/plugins/%{1}

%define autotools_req	%name-plugin-_getdir
%define autotools_summary Automation tool
%define autotools_desc	This plug-in provides some possibilities on automation.
%mkplugin autotools	http://code.google.com/p/rutorrent/wiki/PluginAutotools

%define chunks_summary	Chunks information
%define chunks_desc	This plug-in provides chunks information for opened torrents.
%mkplugin chunks	http://code.google.com/p/rutorrent/wiki/PluginChunks

%define cookies_summary	Cookies information
%define cookies_desc	This plug-in provides cookies information.
%mkplugin cookies	http://code.google.com/p/rutorrent/wiki/PluginCookies

%define cpuload_summary	Show cpu load
%define cpuload_desc	This plug-in adds to status bar an indicator of cpu load.
%mkplugin cpuload	http://code.google.com/p/rutorrent/wiki/PluginCpuload

%define create_req	%name-plugin-_getdir
%define create_summary	Create torrent files
%define create_desc	This plug-in provides ability to create .torrent files.
%mkplugin create	http://code.google.com/p/rutorrent/wiki/PluginCreate

%define data_summary	Transfer downloaded files through http
%define data_desc	This plug-in is intended for obtaining torrent data through http.
%mkplugin data		http://code.google.com/p/rutorrent/wiki/PluginData

%define datadir_req	%name-plugin-_getdir
%define datadir_summary	Move data files
%define datadir_desc	This plug-in is intended for moving torrent's data files.
%mkplugin datadir	http://code.google.com/p/rutorrent/wiki/PluginDataDir

%define diskspace_summary Available disk space
%define diskspace_desc	This plug-in adds to status bar an indicator of available disk space.
%mkplugin diskspace	http://code.google.com/p/rutorrent/wiki/PluginDiskspace

%define edit_summary	Edit torrents
%define edit_desc	This plug-in allows user to edit the list of trackers and commentaries of the current torrent.
%mkplugin edit		http://code.google.com/p/rutorrent/wiki/PluginEdit

%define erasedata_summary Remove data files
%define erasedata_desc	This plug-in allows to remove not only a .torrent file, but also its data.
%mkplugin erasedata	http://code.google.com/p/rutorrent/wiki/PluginErasedata

%define extsearch_summary	External search
%define extsearch_desc	The plug-in is intended for external search of torrents.
%mkplugin extsearch	http://code.google.com/p/rutorrent/wiki/PluginExtsearch

%define feeds_summary	RSS feed creator
%define feeds_desc	The plug-in is intended for making RSS feeds with information of torrents.
%mkplugin feeds		http://code.google.com/p/rutorrent/wiki/PluginFeeds

%define geoip_req	php-geoip
%define geoip_summary	Peer country information
%define geoip_desc	This plug-in provides country information for peers.
%mkplugin geoip		http://code.google.com/p/rutorrent/wiki/PluginGeoIP

%define _getdir_summary	Navigate host system
%define _getdir_desc	This service plug-in _getdir gives to other plug-ins the possibility of comfortable navigation on a host file system.
%mkplugin _getdir	http://code.google.com/p/rutorrent/wiki/Plugin_getdir

%define httprpc_summary	Low-traffic mod_scgi replacement
%define httprpc_desc	This plug-in is designed as a low-traffic replacement of the web server module mod_scgi and performs functions of the last.
%mkplugin httprpc	http://code.google.com/p/rutorrent/wiki/PluginHTTPRPC

%define loginmgr_summary 3rd party login manager
%define loginmgr_desc	The plug-in is intended for managing accounts on private trackers.
%mkplugin loginmgr	http://code.google.com/p/rutorrent/wiki/PluginLoginMgr

%define ratio_summary	Set ratio limits
%define ratio_desc	This plug-in allows to manage a ratio limits for groups of torrents.
%mkplugin ratio		http://code.google.com/p/rutorrent/wiki/PluginRatio

%define retrackers_summary Add custom trackers automatically
%define retrackers_desc	This plug-in appends specified trackers to the trackers list of all newly added torrents.
%mkplugin retrackers	http://code.google.com/p/rutorrent/wiki/PluginRetrackers

%define rpc_summary	mod_scgi replacement
%define rpc_desc	This plug-in is designed as a replacement of the web server module mod_scgi and performs functions of the last.
%mkplugin rpc		http://code.google.com/p/rutorrent/wiki/PluginRPC

%define rss_req		%name-plugin-_getdir
%define rss_summary	RSS feed client
%define rss_desc	This plug-in is intended for work with RSS feeds.
%mkplugin rss		http://code.google.com/p/rutorrent/wiki/PluginRSS

%define rssurlrewrite_req	%name-plugin-rss
%define rssurlrewrite_summary	URL rewriting in the RSS plugin
%define rssurlrewrite_desc	The plug-in is intended for url rewrite in RSS plugin.
%mkplugin rssurlrewrite		http://code.google.com/p/rutorrent/wiki/PluginRSSURLRewrite

%define scheduler_summary Behavior scheduler
%define scheduler_desc	You can enable the scheduler and click the cells to define any of six rTorrent behavior types at each particular hour of 168 week hours.
%mkplugin scheduler	http://code.google.com/p/rutorrent/wiki/PluginScheduler

%define seedingtime_summary Show 'Finished' time
%define seedingtime_desc This plug-in adds the column 'Finished' to the torrents list. This column contains the time when download of the torrent was completed.
%mkplugin seedingtime	http://code.google.com/p/rutorrent/wiki/PluginSeedingtime

%define show_peers_like_wtorrent_summary wTorrent style peer counts
%define show_peers_like_wtorrent_desc	This plug-in changes the format of values in columns 'Seeds' and 'Peers' in the torrents list.
%mkplugin show_peers_like_wtorrent	http://code.google.com/p/rutorrent/wiki/PluginShow_peers_like_wtorrent

%define source_summary	Transfer .torrent file through http
%define source_desc	This plug-in is intended for obtaining source .torrent file.
%mkplugin source	http://code.google.com/p/rutorrent/wiki/PluginSource

%define theme_summary	Theme support for ruTorrent
%define theme_desc	This plugin allows you to change the gui theme to one of several provided themes, or any your create, provided they are placed in the proper directory within the plugin.
%mkplugin theme		http://code.google.com/p/rutorrent/wiki/PluginTheme

%define throttle_summary Torrent group throttling
%define throttle_desc	This plug-in gives a convenient control over a limits of speed for groups of torrents.
%mkplugin throttle	http://code.google.com/p/rutorrent/wiki/PluginThrottle

%define tracklabels_ver	3.0
%define tracklabels_summary Add labels based on trackers
%define tracklabels_desc This plug-in adds a set of labels on the category panel. These labels are created automatically on the basis of torrents' trackers.
%mkplugin tracklabels	http://code.google.com/p/rutorrent/wiki/PluginTracklabels

%define trafic_summary	Traffic statistics
%define trafic_desc	This plug-in is a subsystem for registration of the total (all trackers counted) rTorrent traffic.
%mkplugin trafic	http://code.google.com/p/rutorrent/wiki/PluginTrafic

%define unpack_req	%name-plugin-_getdir
%define unpack_summary	Unpack downloaded data
%define unpack_desc	This plug-in is intended for unpack torrent's data. Packages unzip and unrar are required to unpack those specific formats.
%mkplugin unpack	http://code.google.com/p/rutorrent/wiki/PluginUnpack

%prep
%setup -q -n %name -a 1
%apply_patches
find -name '*.00??*' -print -delete

# make sure a directory layout change is not missed
[ $(ls | wc -l) -eq 10 ]
# make sure the fhs patch does not miss anything
grep -R -e 'conf/' -e "'/share" . && exit 1

# for defaults.patch:
cp -a conf/config.php php/defaults-mdv.php

cat > README.install.urpmi <<EOF
Note that you will need to either configure an SCGI module for your web server
or install rutorrent-plugin-rpc or rutorrent-plugin-httprpc for rutorrent to
work. See the online documentation for more details:
http://code.google.com/p/rutorrent/wiki/WebSERVER

On this Mandriva packaging of rutorrent and its plugins, all configuration
files are in %{_sysconfdir}/%{name}.
The access configuration is in %{_webappconfdir}/%{name}.conf. By default only
localhost is allowed to use rutorrent.
EOF

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_webappconfdir}
cat > %{buildroot}%{_webappconfdir}/%{name}.conf <<EOF
Alias /%{name} %{_datadir}/%{name}

<Directory %{_datadir}/%{name}>
    Require host localhost.localdomain
</Directory>
EOF

install -d -m755 %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/%{name} <<EOF
%{_logdir}/%{name}/*.log {
    missingok
}
EOF

install -d -m755 %{buildroot}%{_datadir}/%{name}
cp -a *.html *.ico css images js lang php plugins %{buildroot}%{_datadir}/%{name}

install -d -m755 %{buildroot}%{_localstatedir}/lib/%{name}
cp -a share %{buildroot}%{_localstatedir}/lib/%{name}

install -d -m755 %{buildroot}%{_sysconfdir}/%{name}
cp -a conf/* %{buildroot}%{_sysconfdir}/%{name}

install -d -m755 %{buildroot}%{_logdir}/%{name}

rm -rf lists
mkdir lists
for dir in %{buildroot}%{_datadir}/%{name}/plugins/*; do
	plugin=$(basename "$dir")
	version=$(sed -n 's,plugin.version: ,,p' "$dir/plugin.info" | tr -d '\r')
	# check that rpm version is set correctly:
	[ "%version" = "$version" ]

	touch lists/$plugin.list
	if [ -e "$dir/conf.php" ]; then
		install -d -m755 %{buildroot}%{_sysconfdir}/%{name}/plugins/$plugin
		cp "$dir/conf.php" %{buildroot}%{_sysconfdir}/%{name}/plugins/$plugin
		mv "$dir/conf.php" "$dir/defaults-mdv.php"
		sed -i '/rtorrent.php.error/s/conf.php/defaults-mdv.php/' $dir/plugin.info
		echo "%dir %{_sysconfdir}/%{name}/plugins/$plugin" >> lists/$plugin.list
		echo "%config(noreplace) %{_sysconfdir}/%{name}/plugins/$plugin/conf.php" >> lists/$plugin.list
	fi
	for file in $dir/readme*.txt; do
		[ -e "$file" ] || continue
		rm "$file"
		echo "%doc plugins/$plugin/$(basename "$file")" >> lists/$plugin.list
	done
done

%clean
rm -rf %{buildroot}

%if %mdkversion < 201010
%post
%_post_webapp

%postun
%_postun_webapp
%endif

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_webappconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/access.ini
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%config(noreplace) %{_sysconfdir}/%{name}/plugins.ini
%dir %{_sysconfdir}/%{name}/plugins
%dir %{_sysconfdir}/%{name}/users
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/css
%{_datadir}/%{name}/favicon.ico
%{_datadir}/%{name}/images
%{_datadir}/%{name}/index.html
%{_datadir}/%{name}/js
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/php
%dir %{_datadir}/%{name}/plugins
%dir %{_localstatedir}/lib/%{name}
%attr(0755,apache,apache) %{_localstatedir}/lib/%{name}/share
%attr(0755,apache,apache) %dir %{_logdir}/%{name}


%changelog
* Sun Dec 12 2010 Anssi Hannula <anssi@mandriva.org> 3.2-2mdv2011.0
+ Revision: 620617
- require apache-conf instead of apache-base for apache user

* Wed Dec 01 2010 Anssi Hannula <anssi@mandriva.org> 3.2-1mdv2011.0
+ Revision: 604521
- initial Mandriva release

