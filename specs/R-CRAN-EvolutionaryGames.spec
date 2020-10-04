%global packname  EvolutionaryGames
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Important Concepts of Evolutionary Game Theory

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.43
BuildRequires:    R-grDevices >= 3.2.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-deSolve >= 1.14
BuildRequires:    R-CRAN-interp >= 1.0.29
BuildRequires:    R-CRAN-rgl >= 0.95.1201
BuildRequires:    R-CRAN-geometry >= 0.3.6
Requires:         R-MASS >= 7.3.43
Requires:         R-grDevices >= 3.2.2
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-deSolve >= 1.14
Requires:         R-CRAN-interp >= 1.0.29
Requires:         R-CRAN-rgl >= 0.95.1201
Requires:         R-CRAN-geometry >= 0.3.6

%description
A comprehensive set of tools to illustrate the core concepts of
evolutionary game theory, such as evolutionary stability or various
evolutionary dynamics, for teaching and academic research.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
