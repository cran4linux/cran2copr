%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CircaCP
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Sleep and Circadian Metrics Estimation from Actigraphy Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
A generic sleep–wake cycle detection algorithm for analyzing unlabeled
actigraphy data. The algorithm has been validated against event markers
using data from the Multi-Ethnic Study of Atherosclerosis (MESA) Sleep
study, and its methodological details are described in Chen and Sun (2024)
<doi:10.1098/rsos.231468>. The package provides functions to estimate
sleep metrics (e.g., sleep and wake onset times) and circadian rhythm
metrics (e.g., mesor, phasor, interdaily stability, intradaily
variability), as well as tools for screening actigraphy quality, fitting
cosinor models, and performing parametric change point detection. The
workflow can also be used to segment long actigraphy sequences into
regularized structures for physical activity research.

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
