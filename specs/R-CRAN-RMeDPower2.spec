%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMeDPower2
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Modeling for Repeated Measures Studies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-simr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-DHARMa 
BuildRequires:    R-CRAN-influence.ME 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-simr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-DHARMa 
Requires:         R-CRAN-influence.ME 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Provides complete functionality to analyse data from repeated measures
experiments with hierarchical or crossed experimental designs. Supports
testing modeling assumptions, identifying outlier observations and
experimental units, estimating statistical power, and performing sample
size calculations. Uses linear mixed effects models via 'lme4' and
simulation-based power analysis via 'simr'. Handles both normal and
non-normal error distributions including binomial and Poisson families.
For more details see Shin et al. (2022) <doi:10.1101/2022.07.18.500490>,
Bates et al. (2015) <doi:10.18637/jss.v067.i01>, Green and MacLeod (2016)
<doi:10.1111/2041-210X.12504>, Hartig (2024)
<doi:10.32614/CRAN.package.DHARMa>, Nieuwenhuis et al. (2012)
<doi:10.32614/RJ-2012-011>, Millard (2013) <doi:10.1007/978-1-4614-8456-1>
and Kuznetsova et al. (2017) <doi:10.18637/jss.v082.i13>.

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
