%global packname  spind
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Methods and Indices

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.49
BuildRequires:    R-CRAN-gee >= 4.13.19
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-splancs >= 2.1.40
BuildRequires:    R-CRAN-rje >= 1.9
BuildRequires:    R-CRAN-waveslim >= 1.7.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-geepack >= 1.2.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-CRAN-lattice >= 0.20.35
BuildRequires:    R-CRAN-rlang >= 0.2.1
Requires:         R-CRAN-MASS >= 7.3.49
Requires:         R-CRAN-gee >= 4.13.19
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-splancs >= 2.1.40
Requires:         R-CRAN-rje >= 1.9
Requires:         R-CRAN-waveslim >= 1.7.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-geepack >= 1.2.1
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-CRAN-lattice >= 0.20.35
Requires:         R-CRAN-rlang >= 0.2.1

%description
Functions for spatial methods based on generalized estimating equations
(GEE) and wavelet-revised methods (WRM), functions for scaling by wavelet
multiresolution regression (WMRR), conducting multi-model inference, and
stepwise model selection. Further, contains functions for spatially
corrected model accuracy measures.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
