%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tlsR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detection and Spatial Analysis of Tertiary Lymphoid Structures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-spatstat.explore >= 3.0.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.0.0
BuildRequires:    R-CRAN-fastICA >= 1.2.3
BuildRequires:    R-CRAN-FNN >= 1.1.3
BuildRequires:    R-CRAN-dbscan >= 1.1.10
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-spatstat.explore >= 3.0.0
Requires:         R-CRAN-spatstat.geom >= 3.0.0
Requires:         R-CRAN-fastICA >= 1.2.3
Requires:         R-CRAN-FNN >= 1.1.3
Requires:         R-CRAN-dbscan >= 1.1.10
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Fast, reproducible detection and quantitative analysis of tertiary
lymphoid structures (TLS) in multiplexed tissue imaging. Implements
Independent Component Analysis Trace (ICAT) index, local Ripley's K
scanning, automated K Nearest Neighbor (KNN)-based TLS detection, and
T-cell clusters identification as described in Amiryousefi et al. (2025)
<doi:10.1101/2025.09.21.677465>.

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
