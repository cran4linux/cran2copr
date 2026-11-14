%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lactater
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Lactate Thresholds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-ggtext >= 0.2.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-pillar 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-ggtext >= 0.2.0
Requires:         R-grid 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-pillar 
Requires:         R-CRAN-rlang 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
Set of tools for analyzing lactate thresholds from a step incremental test
to exhaustion. Estimate Log-log, Onset of Blood Lactate Accumulation
(OBLA), Baseline plus (Bsln+), the Dmax family, Lactate Turn Points (LTP),
the Lactate / Intensity ratio (LTratio), and the Individual Anaerobic
Thresholds of Dickhuth (IAT) and Stegmann in cycling, running, swimming,
or rowing, with bootstrap confidence intervals, data-quality checks,
training zones, test comparisons, training load, and the maximal lactate
accumulation rate (VLamax). Beaver WL, Wasserman K, Whipp BJ (1985)
<doi:10.1152/jappl.1985.59.6.1936>. Heck H, Mader A, Hess G, Mücke S,
Müller R, Hollmann W (1985) <doi:10.1055/s-2008-1025824>. Kindermann W,
Simon G, Keul J (1979) <doi:10.1007/BF00421101>. Skinner JS, Mclellan TH
(1980) <doi:10.1080/02701367.1980.10609285>. Berg A, Jakob E, Lehmann M,
Dickhuth HH, Huber G, Keul J (1990) PMID 2408033. Zoladz JA, Rademaker AC,
Sargeant AJ (1995) <doi:10.1113/jphysiol.1995.sp020959>. Cheng B, Kuipers
H, Snyder A, Keizer H, Jeukendrup A, Hesselink M (1992)
<doi:10.1055/s-2007-1021309>. Bishop D, Jenkins DG, Mackinnon LT (1998)
<doi:10.1097/00005768-199808000-00014>. Hughson RL, Weisiger KH, Swanson
GD (1987) <doi:10.1152/jappl.1987.62.5.1975>. Jamnick NA, Botella J, Pyne
DB, Bishop DJ (2018) <doi:10.1371/journal.pone.0199794>. Hofmann P,
Tschakert G (2017) <doi:10.3389/fphys.2017.00337>. Hofmann P, Pokan R, von
Duvillard SP, Seibert FJ, Zweiker R, Schmid P (1997)
<doi:10.1097/00005768-199706000-00005>. Pokan R, Hofmann P, Von Duvillard
SP, et al. (1997) <doi:10.1097/00005768-199708000-00009>. Dickhuth H-H,
Yin L, Niess A, et al. (1999) <doi:10.1055/s-2007-971105>. Stegmann H,
Kindermann W, Schnabel A (1981) <doi:10.1055/s-2008-1034604>. Heuberger
JAAC, Gal P, Stuurman FE, et al. (2018)
<doi:10.1371/journal.pone.0206846>. Meixner B, Nusser V, Koehler K, et al.
(2024) <doi:10.14814/phy2.16086>.

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
