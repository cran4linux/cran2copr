%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ncvreg
%global packver   3.14.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.14.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regularization Paths for SCAD and MCP Penalized Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Fits regularization paths for linear regression, GLM, and Cox regression
models using lasso or nonconvex penalties, in particular the minimax
concave penalty (MCP) and smoothly clipped absolute deviation (SCAD)
penalty, with options for additional L2 penalties (the "elastic net"
idea). Utilities for carrying out cross-validation as well as post-fitting
visualization, summarization, inference, and prediction are also provided.
For more information, see Breheny and Huang (2011)
<doi:10.1214/10-AOAS388> or visit the ncvreg homepage
<https://pbreheny.github.io/ncvreg/>.

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
