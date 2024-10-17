%define	name	bumprace
%define	version	1.5.3
%define release	4

Summary:	Drive the ship to exit
Name:		%{name}
Epoch:		1
Version:	%{version}
Release:	%{release}
Source0:	http://www.linux-games.com/bumprace/bumprace-%{version}.tar.gz
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
License:	GPLv2+
Group:		Games/Arcade
Url:		https://www.linux-games.com/bumprace
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}buildroot

%description
BumpRace is a simple arcade game. You've to get from the start to the finish
line without crashing into deadly blocks. This game is really easy to learn!

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Bumprace
Comment=%{summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -D -m644 %SOURCE6 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m644 %SOURCE5 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -D -m644 %SOURCE7 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS FAQ NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1:1.5.3-3mdv2011.0
+ Revision: 635080
- fix typo
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.3-2mdv2011.0
+ Revision: 616904
- the mass rebuild of 2010.0 packages

* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 1:1.5.3-1mdv2010.0
+ Revision: 376114
- add missing buildrequires
- new version 1.5.3

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.45-13mdv2009.0
+ Revision: 243373
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Funda Wang <fwang@mandriva.org> 1.45-11mdv2008.1
+ Revision: 116847
- drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - buildrequires X11-devel instead of XFree86-devel
    - import bumprace


* Fri Jul  7 2006 Pixel <pixel@mandriva.com> 1.45-10mdv2007.0
- use mkrel
- switch to XDG menu

* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 1.45-9mdk
- rebuild for sparc

* Tue Oct 11 2005 Pixel <pixel@mandriva.com> 1.45-8mdk
- rebuild

* Fri Aug 13 2004 Pixel <pixel@mandrakesoft.com> 1.45-7mdk
- rebuild

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.45-6mdk
- rebuild

* Thu Nov 12 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 1.45-5mdk
- Cleanups
- Removed (extremely) redundant Buildrequires
- Moved stuff to correct places
- Added menuentry
- Added icons
- Cleanups

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.45-4mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.45-3mdk
- Automated rebuild with gcc3.2

* Sun Jul 21 2002 Pixel <pixel@mandrakesoft.com> 1.45-2mdk
- recompile against new vorbis stuff

* Thu Jun 27 2002 Pixel <pixel@mandrakesoft.com> 1.45-1mdk
- new release

* Mon Apr 29 2002 Pixel <pixel@mandrakesoft.com> 1.43-2mdk
- rebuild for new libasound (alsa)

* Sat Feb  2 2002 Pixel <pixel@mandrakesoft.com> 1.43-1mdk
- new release

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 1.42-6mdk
- BuildRequires

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.42-5mdk
- rebuilding for libpng3

* Fri Sep 28 2001 Stefan van der Eijk <stefan@eijk.nu> 1.42-4mdk
- BuildRequires: libjpeg-devel libpng-devel libSDL-devel

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 1.42-3mdk
- rebuild

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 1.42-2mdk
- rebuild with new SDL

* Fri Mar 30 2001 Pixel <pixel@mandrakesoft.com> 1.42-1mdk
- new version

* Thu Dec 21 2000 Pixel <pixel@mandrakesoft.com> 1.4-4mdk
- capitalize summary

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 1.4-3mdk
- rebuild for new lib mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 1.4-2mdk
- rebuild, build req

* Sun Oct 22 2000 Pixel <pixel@mandrakesoft.com> 1.4-1mdk
- initial spec
