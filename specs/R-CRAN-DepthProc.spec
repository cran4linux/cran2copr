%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DepthProc
%global packver   2.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Depth Functions for Multivariate Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rrcov 
Requires:         R-methods 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-np 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-zoo 
Requires:         R-grDevices 

%description
Data depth concept offers a variety of powerful and user friendly tools
for robust exploration and inference for multivariate data. The offered
techniques may be successfully used in cases of lack of our knowledge on
parametric models generating data due to their nature. The package consist
of among others implementations of several data depth techniques involving
multivariate quantile-quantile plots, multivariate scatter estimators,
multivariate Wilcoxon tests and robust regressions.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
