%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multilandr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Landscape Analysis at Multiple Spatial Scales

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.3.0
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-GGally >= 2.2.1
BuildRequires:    R-CRAN-landscapemetrics >= 2.1.1
BuildRequires:    R-CRAN-terra >= 1.7.71
BuildRequires:    R-CRAN-sf >= 1.0.16
BuildRequires:    R-CRAN-tidyterra >= 0.6.0
Requires:         R-methods >= 4.3.0
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-GGally >= 2.2.1
Requires:         R-CRAN-landscapemetrics >= 2.1.1
Requires:         R-CRAN-terra >= 1.7.71
Requires:         R-CRAN-sf >= 1.0.16
Requires:         R-CRAN-tidyterra >= 0.6.0

%description
Provides a tidy workflow for landscape-scale analysis. 'multilandr' offers
tools to generate landscapes at multiple spatial scales and compute
landscape metrics, primarily using the 'landscapemetrics' package. It also
features utility functions for plotting and analyzing multi-scale
landscapes, exploring correlations between metrics, filtering landscapes
based on specific conditions, generating landscape gradients for a given
metric, and preparing datasets for further statistical analysis.
Documentation about 'multilandr' is provided in an introductory vignette
included in this package and in the paper by Huais (2024)
<doi:10.1007/s10980-024-01930-z>; see citation("multilandr") for details.

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
