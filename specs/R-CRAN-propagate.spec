%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  propagate
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Propagation of Uncertainty

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-hdf5r 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-hdf5r 
Requires:         R-CRAN-crayon 

%description
Propagation of uncertainty using higher-order Taylor expansion and Monte
Carlo simulation. Calculations of propagated uncertainties are based on
matrix calculus including covariance structure according to Arras 1998
<doi:10.3929/ethz-a-010113668> (first order), Wang & Iyer 2005
<doi:10.1088/0026-1394/42/5/011> (second order) and BIPM Supplement 1
(Monte Carlo) <doi:10.59161/JCGM101-2008>.

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
