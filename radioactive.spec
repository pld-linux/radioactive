Summary:	A FM-Tuner program for Gnome
Summary(pl):	Tuner FM dla Gnome
Name:		radioactive
Version:	1.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://cactus.rulez.org/projects/radioactive/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fixes.patch
URL:		http://cactus.rulez.org/projects/radioactive/
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnomemm-devel
BuildRequires:	gtkmm-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	panelmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
RadioActive is a small radio application for Video4Linux-compatible
radio tuner cards. The lowlevel functions were initially based on
GRadio, but RadioActive has a traditional, real-world radio-like
interface.

%description -l pl
RadioActive to niewielka aplikacja radiowa dla tunerów kompatybilnych
z interfejsem Video4Linux. Niskopoziomowe funkcje bazuj± na GRadio ale
RadioActive ma w³asny, tradycyjny interfejs.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
xml-i18n-toolize --copy --force
aclocal -I %{_aclocaldir}/gnome
autoconf
automake -a -c
#CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti`"
%configure \
	--with-applet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Desktopdir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_datadir}/applets/Multimedia/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*.desktop
