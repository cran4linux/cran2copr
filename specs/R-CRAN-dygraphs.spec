%global __brp_check_rpaths %{nil}
%global packname  dygraphs
%global packver   1.1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Interface to 'Dygraphs' Interactive Time Series Charting Library

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zoo >= 1.7.10
BuildRequires:    R-CRAN-xts >= 0.9.7
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-htmltools >= 0.3.5
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-zoo >= 1.7.10
Requires:         R-CRAN-xts >= 0.9.7
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-magrittr 

%description
An R interface to the 'dygraphs' JavaScript charting library (a copy of
which is included in the package). Provides rich facilities for charting
time-series data in R, including highly configurable series- and
axis-display and interactive features like zoom/pan and series/point
highlighting.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYING
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NOTICE
%doc %{rlibdir}/%{packname}/plotters
%doc %{rlibdir}/%{packname}/plugins
%{rlibdir}/%{packname}/INDEX
