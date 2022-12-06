%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metanetwork
%global packver   0.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Handling and Representing Trophic Networks in Space and Time

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-intergraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggimage 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sna 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-network 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-intergraph 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-visNetwork 
Requires:         R-grDevices 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggimage 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sna 

%description
A toolbox to handle and represent trophic networks in space or time across
aggregation levels. This package contains a layout algorithm specifically
designed for trophic networks, using dimension reduction on a diffusion
graph kernel and trophic levels. Importantly, this package provides a
layout method applicable for large trophic networks.

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
