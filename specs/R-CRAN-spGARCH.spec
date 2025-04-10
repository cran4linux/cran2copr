%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spGARCH
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial ARCH and GARCH Models (spGARCH)

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-stats 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-Rsolnp 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nleqslv 
Requires:         R-methods 
Requires:         R-CRAN-crayon 

%description
A collection of functions to deal with spatial and spatiotemporal
autoregressive conditional heteroscedasticity (spatial ARCH and GARCH
models) by Otto, Schmid, Garthoff (2018, Spatial Statistics)
<doi:10.1016/j.spasta.2018.07.005>: simulation of spatial ARCH-type
processes (spARCH, log/exponential-spARCH, complex-spARCH);
quasi-maximum-likelihood estimation of the parameters of spARCH models and
spatial autoregressive models with spARCH disturbances, diagnostic checks,
visualizations.

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
