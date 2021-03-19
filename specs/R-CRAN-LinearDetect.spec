%global packname  LinearDetect
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Change Point Detection in High-Dimensional Linear Regression Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-factoextra 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-sparsevar 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-factoextra 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-sparsevar 

%description
A unified framework for simultaneous structural break detection and
parameter estimation in high-dimensional linear models. The proposed
method can handle a wide range of models, including change-in-mean model,
multiple linear regression model, Vector auto-regressive model and
Gaussian graphical model.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
