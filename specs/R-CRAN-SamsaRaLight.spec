%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SamsaRaLight
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Tree Light Transmission Using Ray-Tracing

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-concaveman 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-concaveman 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-ggnewscale 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-CRAN-tidyr 

%description
Provides tools to simulate light transmission in forest stands using
three-dimensional ray-tracing. The package allows users to build virtual
stands from tree inventories and to estimate (1) light intercepted by
individual trees, (2) light reaching the forest floor, and (3) light at
virtual sensors. The package is designed for ecological and forestry
applications, including the analysis of light competition, tree growth,
and forest regeneration. The implementation builds on the individual-based
ray-tracing model SamsaraLight developed by Courbaud et al. (2003)
<doi:10.1016/S0168-1923(02)00254-X>.

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
