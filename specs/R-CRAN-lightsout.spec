%global __brp_check_rpaths %{nil}
%global packname  lightsout
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Implementation of the 'Lights Out' Puzzle Game

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-shinyjs >= 0.3.0
BuildRequires:    R-CRAN-shiny >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-shinyjs >= 0.3.0
Requires:         R-CRAN-shiny >= 0.10.0
Requires:         R-stats 
Requires:         R-utils 

%description
Lights Out is a puzzle game consisting of a grid of lights that are either
on or off. Pressing any light will toggle it and its adjacent lights. The
goal of the game is to switch all the lights off. This package provides an
interface to play the game on different board sizes, both through the
command line or with a visual application. Puzzles can also be solved
using the automatic solver included. View a demo online at
http://daattali.com/shiny/lightsout/.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
