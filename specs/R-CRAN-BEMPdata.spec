%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BEMPdata
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Access the Bangladesh Environmental Mobility Panel Dataset

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-shiny 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-shiny 

%description
Provides functions to download and work with the Bangladesh Environmental
Mobility Panel (BEMP), a household panel survey tracing the impacts of
riverbank erosion and flooding on (im)mobility, socio-economic outcomes,
and political attitudes along the Jamuna River in Bangladesh (2021-2024).
Wave datasets (20 files across 14 survey rounds) are hosted on Zenodo
(<https://zenodo.org/records/18229498>) and downloaded on demand with
local caching. Bundled data include a merged cross-wave codebook and wave
metadata.

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
