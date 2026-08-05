%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lame
%global packver   1.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal Additive and Multiplicative Effects Models for Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-netify >= 1.5.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-netify >= 1.5.3
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Additive and multiplicative effects models for both cross-sectional and
longitudinal network analysis. The package provides two main functions:
ame() for cross-sectional networks and lame() for longitudinal networks.
It supports square and rectangular network structures. Key features
include: (1) Cross-sectional network analysis via ame() with support for
binary, continuous, ordinal, and count data; (2) Longitudinal network
analysis via lame() with additive sender/receiver and multiplicative
latent-factor effects that can evolve over time through AR(1) processes
(Sewell and Chen (2015) <doi:10.1080/01621459.2014.988214>; Durante and
Dunson (2014) <doi:10.1093/biomet/asu040>); (3) Handling of changing actor
compositions across time periods in longitudinal models; (4) Performance
improvements through C++ implementations via 'Rcpp' and 'RcppArmadillo'.

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
