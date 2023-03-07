%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shoredate
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Shoreline Dating Stone Age Sites on the Norwegian Skagerrak Coast

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-ggsn 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-ggsn 
Requires:         R-grid 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Provides tools for shoreline dating Stone Age sites located on the
Norwegian Skagerrak coast using methods presented in Roalkvam (2023)
<doi:10.1016/j.quascirev.2022.107880>. Shoreline dating is based on the
present-day elevation of a site, a reconstruction of past relative
sea-level change, and empirically derived estimates of the likely
elevation of the sites above the contemporaneous sea-level when they were
in use. The geographical and temporal coverage of the method thus follows
from local geological reconstructions of shoreline displacement and the
degree to which settlements in the region have been found to have been
located on or close to the shoreline when they were in use. Methods for
numerical treatment and visualisation of the dates are provided, along
with basic tools for evaluating the location of sites within the region
and corresponding variation in local shoreline displacement.

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
