Summary:	A fraktal tree
Summary(pl):	Drzewko fraktalne
Name:		drzefko
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

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
	CFLAGS="%{rpmcflags} `sdl-config --cflags`" \
	LDFLAGS="%{rpmldflags} `sdl-config --libs` -lGL -lGLU"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Amusements}
install drzefko $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

install drzefko.png $RPM_BUILD_ROOT%{_pixmapsdir}
cat <<EOF > $RPM_BUILD_ROOT%{_applnkdir}/Amusements/drzefko.desktop
[Desktop Entry]
Name=drzefko
Comment=A fractal tree
Comment[pl]=Drzewko fraktalne
Icon=drzefko.png
Exec=drzefko
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%lang(pl) %doc README.gz
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*
