%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HVT
%global packver   23.11.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          23.11.1
Release:          1%{?dist}%{?buildtag}
Summary:          Constructing Hierarchical Voronoi Tessellations and Overlay Heatmaps for Data Analysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-conf.design 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-polyclip 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-deldir 
Requires:         R-grDevices 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-conf.design 
Requires:         R-CRAN-Hmisc 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-polyclip 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 

%description
Facilitates building topology preserving maps for rich multivariate data.
See <https://en.wikipedia.org/wiki/Voronoi_diagram> for more information.
Credits to Mu Sigma for their continuous support throughout the
development of the package.

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
