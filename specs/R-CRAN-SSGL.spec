%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SSGL
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Spike-and-Slab Group Lasso for Group-Regularized Generalized Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-grpreg 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-grpreg 

%description
Fits group-regularized generalized linear models (GLMs) using the
spike-and-slab group lasso (SSGL) prior introduced by Bai et al. (2022)
<doi:10.1080/01621459.2020.1765784> and extended to GLMs by Bai (2023)
<arXiv:2007.07021>. This package supports fitting the SSGL model for the
following GLMs with group sparsity: Gaussian linear regression, binary
logistic regression, Poisson regression, negative binomial regression, and
gamma regression. Stand-alone functions for group-regularized negative
binomial regression and group-regularized gamma regression are also
available, with the option of employing the group lasso penalty of Yuan
and Lin (2006) <doi:10.1111/j.1467-9868.2005.00532.x>, the group minimax
concave penalty (MCP) of Breheny and Huang
<doi:10.1007/s11222-013-9424-2>, or the group smoothly clipped absolute
deviation (SCAD) penalty of Breheny and Huang (2015)
<doi:10.1007/s11222-013-9424-2>.

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
