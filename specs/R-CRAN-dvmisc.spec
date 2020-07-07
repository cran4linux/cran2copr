%global packname  dvmisc
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}
Summary:          Convenience Functions, Moving Window Statistics, and Graphics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-rbenchmark 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-tab 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-rbenchmark 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-tab 
Requires:         R-utils 

%description
Contains functions that do something convenient (e.g. create BMI
categories), functions for calculating moving-window statistics
efficiently, and functions for generating various figures (e.g. histograms
with fitted probability mass/density function).

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
%{rlibdir}/%{packname}/libs
