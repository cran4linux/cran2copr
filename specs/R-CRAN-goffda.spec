%global __brp_check_rpaths %{nil}
%global packname  goffda
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Tests for Functional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ks 

%description
Implementation of several goodness-of-fit tests for functional data.
Currently, mostly related with the functional linear model with
functional/scalar response and functional/scalar predictor. The package
allows for the replication of the data applications considered in
García-Portugués, Álvarez-Liébana, Álvarez-Pérez and González-Manteiga
(2019) <arXiv:1909.07686>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
