%global packname  ncvreg
%global packver   3.12.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.12.0
Release:          1%{?dist}
Summary:          Regularization Paths for SCAD and MCP Penalized RegressionModels

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
