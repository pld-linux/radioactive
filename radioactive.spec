Summary:	A FM-Tuner program for Gnome
Summary(pl):	Tuner FM dla Gnome
Name:		radioactive
Version:	1.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://cactus.rulez.org/projects/radioactive/download/%{name}-%{version}.tar.gz
URL:		http://cactus.rulez.org/projects/radioactive/
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	ORBit-devel
BuildRequires:	gtkmm-devel
BuildRequires:	gnomemm-devel
BuildRequires:	panelmm-devel
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions `orbit-config --cflags client`"; export CXXFLAGS
%configure2_13 \
	--with-applet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*.desktop
