%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PVplr
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Performance Loss Rate Analysis Pipeline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-cluster >= 2.0.7.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-tidyr >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-broom >= 0.5.1
BuildRequires:    R-CRAN-stlplus >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-rlang >= 0.3.1
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-cluster >= 2.0.7.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-tidyr >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-broom >= 0.5.1
Requires:         R-CRAN-stlplus >= 0.5.1
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-zoo 

%description
The pipeline contained in this package provides tools used in the Solar
Durability and Lifetime Extension Center (SDLE) for the analysis of
Performance Loss Rates (PLR) in real world photovoltaic systems. Functions
included allow for data cleaning, feature correction, power predictive
modeling, PLR determination, and uncertainty bootstrapping through various
methods <doi:10.1109/PVSC40753.2019.8980928>. The vignette "Pipeline
Walkthrough" gives an explicit run through of typical package usage. This
material is based upon work supported by the U.S Department of Energy's
Office of Energy Efficiency and Renewable Energy (EERE) under Solar Energy
Technologies Office (SETO) Agreement Number DE-EE-0008172. This work made
use of the High Performance Computing Resource in the Core Facility for
Advanced Research Computing at Case Western Reserve University.

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
