%global packname  rpanel
%global packver   1.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          2%{?dist}
Summary:          Simple Interactive Controls for R using the 'tcltk' Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    bwidget
Requires:         bwidget
BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
Requires:         R-tcltk 

%description
A set of functions to build simple GUI controls for R functions.  These
are built on the 'tcltk' package. Uses could include changing a parameter
on a graph by animating it with a slider or a "doublebutton", up to more
sophisticated control panels. Some functions for specific graphical tasks,
referred to as 'cartoons', are provided.

%prep
%setup -q -c -n %{packname}


%build

%install
Xvfb :0 &
XVFB_PID=$!
export DISPLAY=:0
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} && kill $XVFB_PID
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/history.txt
%doc %{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/INDEX
