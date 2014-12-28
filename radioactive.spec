Summary:	A FM-Tuner program for GNOME
Summary(pl.UTF-8):	Tuner FM dla GNOME
Name:		radioactive
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://cactus.rulez.org/projects/radioactive/download/%{name}-%{version}.tar.gz
# Source0-md5:	5f634b16825c24bd613736c2d5aa3591
URL:		http://cactus.rulez.org/projects/radioactive/
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnomemm-devel
BuildRequires:	gtkmm1-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	panelmm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

%description
RadioActive is a small radio application for Video4Linux-compatible
radio tuner cards. The lowlevel functions were initially based on
GRadio, but RadioActive has a traditional, real-world radio-like
interface.

%description -l pl.UTF-8
RadioActive to niewielka aplikacja radiowa dla tunerów kompatybilnych
z interfejsem Video4Linux. Niskopoziomowe funkcje bazują na GRadio ale
RadioActive ma własny, tradycyjny interfejs.

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
