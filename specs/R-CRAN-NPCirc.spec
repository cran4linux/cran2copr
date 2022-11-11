%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NPCirc
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Circular Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.8.3
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-CRAN-Bolstad2 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.8.3
Requires:         R-CRAN-circular 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-shape 
Requires:         R-CRAN-Bolstad2 

%description
Nonparametric smoothing methods for density and regression estimation
involving circular data, including the estimation of the mean regression
function and other conditional characteristics.

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
