%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  circda
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Circular Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-Directional 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rangen 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-Directional 
Requires:         R-CRAN-glmnet 
Requires:         R-graphics 
Requires:         R-CRAN-rangen 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Functions to perform maximum likelihood estimation, model-based
clustering, discriminant and regression analysis with a circular response
variable.  The standard textbook for such data is the "Directional
Statistics" by Mardia, K. V. and Jupp, P. E. (2000). Other references
include: Tsagris M. and Alzeley O. (2025). "Circular and spherical
projected Cauchy distributions: A Novel Framework for Circular and
Directional Data Modeling". Australian & New Zealand Journal of
Statistics, 67(1): 77--103. <doi:10.1111/anzs.12434>. Tsagris M.,
Papastamoulis P. and Kato S. (2025). "Directional data analysis: spherical
Cauchy or Poisson kernel-based distribution". Statistics and Computing,
35:51 <doi:10.1007/s11222-025-10583-0>. Alzeley O. and Tsagris (2026). "On
the generalized circular projected Cauchy distribution". Mathematics,
14(11): 1934 <doi:10.3390/math14111934>.

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
