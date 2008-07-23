%define	name	bumprace
%define	version	1.45
%define release	%mkrel 13

Summary:	Drive the ship to exit
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.linux-games.com/bumprace/bumprace-%{version}.tar.bz2
Source5:	%{name}-16.png
Source6:	%{name}-32.png
Source7:	%{name}-48.png
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.linux-games.com/bumprace
BuildRequires:	SDL_mixer-devel X11-devel alsa-lib-devel esound-devel
BuildRequires:	libjpeg-devel libpng-devel texinfo
BuildRoot:	%{_tmppath}/%{name}-%{version}buildroot

%description
BumpRace is a simple arcade game. You've to get from the start to the finish
line without crashing into deadly blocks. This game is really easy to learn!

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
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
