Summary:	A fraktal tree
Summary(pl):	Drzewko fraktalne
Name:		drzefko
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://team.pld.org.pl/~wolf/drzefko/s/%{name}-%{version}.tar.gz
# Source0-md5:	63ce5abff0da967283f061622d781017
Source1:	%{name}.desktop
URL:		http://team.pld.org.pl/~wolf/drzefko/
BuildRequires:	SDL-devel
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Toy showing use of fractals. Warning: GeForce class 3D accelerator is
recommended (but not required -- it was developed on Voodoo.)

%description -l pl
Zabawka pokazuj±ca u¿ycie fraktali. Uwaga: akcelerator klasy GeForce
jest zalecany (ale nie wymagany -- program by³ pisany pod Voodoo.)

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` -I/usr/X11R6/include -DDATADIR=\\\"%{_datadir}/drzefko/\\\" -DVERSION=\\\"%{version}\\\"" \
	LDFLAGS="%{rpmldflags} `sdl-config --libs` -lGL -lGLU -lSDL_image"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Amusements,%{_datadir}/drzefko}

install drzefko $RPM_BUILD_ROOT%{_bindir}
install lisc.png $RPM_BUILD_ROOT%{_datadir}/drzefko/

install drzefko.png $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Amusements

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%lang(pl) %doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/drzefko
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*
