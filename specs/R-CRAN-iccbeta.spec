%global __brp_check_rpaths %{nil}
%global packname  iccbeta
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multilevel Model Intraclass Correlation for Slope Heterogeneity

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.200
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-lme4 
Requires:         R-stats 
Requires:         R-methods 

%description
A function and vignettes for computing an intraclass correlation described
in Aguinis & Culpepper (2015) <doi:10.1177/1094428114563618>. This package
quantifies the share of variance in a dependent variable that is
attributed to group heterogeneity in slopes.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
