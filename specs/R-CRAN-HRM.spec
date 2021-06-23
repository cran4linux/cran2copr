%global __brp_check_rpaths %{nil}
%global packname  HRM
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          High-Dimensional Repeated Measures

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-pseudorank >= 0.3.8
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-pseudorank >= 0.3.8
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-MASS 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-reshape2 
Requires:         R-tcltk 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-mvtnorm 

%description
Methods for testing main and interaction effects in possibly
high-dimensional parametric or nonparametric repeated measures in
factorial designs for univariate or multivariate data. The observations of
the subjects are assumed to be multivariate normal if using the parametric
test. The nonparametric version tests with regard to nonparametric
relative effects (based on pseudo-ranks). It is possible to use up to 2
whole- and 3 subplot factors.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
