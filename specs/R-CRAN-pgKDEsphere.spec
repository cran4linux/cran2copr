%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pgKDEsphere
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parametrically Guided Kernel Density Estimator for Spherical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.11
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-CRAN-DirStats 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-rotasym 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.11
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Directional 
Requires:         R-CRAN-DirStats 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-rotasym 
Requires:         R-CRAN-movMF 

%description
Nonparametric density estimation for (hyper)spherical data by means of a
parametrically guided kernel estimator (adaptation of the method of Hjort
and Glad (1995) <doi:10.1214/aos/1176324627> to the spherical setting).
The package also allows the data-driven selection of the smoothing
parameter and the representation of the estimated density for circular and
spherical data. Estimators of the density without guide can also be
obtained.

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
