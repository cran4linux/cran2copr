%global __brp_check_rpaths %{nil}
%global packname  clogitL1
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Fitting Exact Conditional Logistic Regression with Lasso andElastic Net Penalties

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
Requires:         R-CRAN-Rcpp >= 0.10.2

%description
Tools for the fitting and cross validation of exact conditional logistic
regression models with lasso and elastic net penalties. Uses cyclic
coordinate descent and warm starts to compute the entire path efficiently.

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
