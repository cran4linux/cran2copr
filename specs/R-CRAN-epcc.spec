%global __brp_check_rpaths %{nil}
%global packname  epcc
%global packver   1.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Populations of Ectotherms under Global Warming

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-raster >= 3.1.5
BuildRequires:    R-CRAN-rgdal >= 1.5.10
BuildRequires:    R-CRAN-sp >= 1.4.5
BuildRequires:    R-CRAN-httr >= 1.4.2
BuildRequires:    R-CRAN-readxl >= 1.3.1
BuildRequires:    R-CRAN-deSolve >= 1.28
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-proto >= 1.0.0
BuildRequires:    R-CRAN-formattable >= 0.2.1
BuildRequires:    R-CRAN-nls2 >= 0.2
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-raster >= 3.1.5
Requires:         R-CRAN-rgdal >= 1.5.10
Requires:         R-CRAN-sp >= 1.4.5
Requires:         R-CRAN-httr >= 1.4.2
Requires:         R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-deSolve >= 1.28
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-proto >= 1.0.0
Requires:         R-CRAN-formattable >= 0.2.1
Requires:         R-CRAN-nls2 >= 0.2
Requires:         R-CRAN-rlang 

%description
Provides several functions that allow model and simulate the effects of
thermal sensitivity and the exposition to different trends in
environmental temperature on the abundance dynamics of ectotherms
populations. It allows an easy implementation of the possible consequences
of warming at global and local scales, constituting a useful tool for
understanding the extinction risk of populations. (Víctor Saldaña-Núñez,
Fernando Córdova-Lepe, & Felipe N. Moreno-Gómez, 2021)
<doi:10.5281/zenodo.5034087>.

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
