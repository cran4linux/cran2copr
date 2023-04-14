%global __brp_check_rpaths %{nil}
%global packname  EWGoF
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for the Exponential and Two-ParameterWeibull Distributions

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-Rcpp >= 0.10.3

%description
Contains a large number of the goodness-of-fit tests for the Exponential
and Weibull distributions classified into families: the tests based on the
empirical distribution function, the tests based on the probability plot,
the tests based on the normalized spacings, the tests based on the Laplace
transform and the likelihood based tests.

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
