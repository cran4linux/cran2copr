%global packname  ecr
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          2%{?dist}
Summary:          Evolutionary Computation in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-smoof >= 1.4
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-ParamHelpers >= 1.1
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-smoof >= 1.4
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-ParamHelpers >= 1.1
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-ggplot2 >= 1.0.0

%description
Framework for building evolutionary algorithms for both single- and
multi-objective continuous or discrete optimization problems. A set of
predefined evolutionary building blocks and operators is included.
Moreover, the user can easily set up custom objective functions,
operators, building blocks and representations sticking to few
conventions. The package allows both a black-box approach for standard
tasks (plug-and-play style) and a much more flexible white-box approach
where the evolutionary cycle is written by hand.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
