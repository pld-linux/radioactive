Summary:	A FM-Tuner program for Gnome
Summary(pl):	Tuner FM dla Gnome
Name:		radioactive
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://cactus.rulez.org/projects/radioactive/download/%{name}-%{version}.tar.gz
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

%build
rm -f missing
%{__gettextize}
xml-i18n-toolize --copy --force
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
#CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti`"
%configure \
	--with-applet
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Desktopdir=%{_applnkdir}/Multimedia

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/CORBA/servers/*
%{_pixmapsdir}/*
%{_applnkdir}/Multimedia/*
