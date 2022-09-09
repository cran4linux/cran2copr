%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lactater
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Analyzing Lactate Thresholds

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggtext 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggtext 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-forcats 

%description
Set of tools for analyzing lactate thresholds from a step incremental test
to exhaustion. Easily analyze the methods Log-log, Onset of Blood Lactate
Accumulation (OBLA), Baseline plus (Bsln+), Dmax, Lactate Turning Point
(LTP), and Lactate / Intensity ratio (LTratio) in cycling, running, or
swimming. Beaver WL, Wasserman K, Whipp BJ (1985)
<doi:10.1152/jappl.1985.59.6.1936>. Heck H, Mader A, Hess G, Mücke S,
Müller R, Hollmann W (1985) <doi:10.1055/s-2008-1025824>. Kindermann W,
Simon G, Keul J (1979) <doi:10.1007/BF00421101>. Skinner JS, Mclellan TH
(1980) <doi:10.1080/02701367.1980.10609285>. Berg A, Jakob E, Lehmann M,
Dickhuth HH, Huber G, Keul J (1990) <PMID:2408033>. Zoladz JA, Rademaker
AC, Sargeant AJ (1995) <doi:10.1113/jphysiol.1995.sp020959>. Cheng B,
Kuipers H, Snyder A, Keizer H, Jeukendrup A, Hesselink M (1992)
<doi:10.1055/s-2007-1021309>. Bishop D, Jenkins DG, Mackinnon LT (1998)
<doi:10.1097/00005768-199808000-00014>. Hughson RL, Weisiger KH, Swanson
GD (1987) <doi:10.1152/jappl.1987.62.5.1975>. Jamnick NA, Botella J, Pyne
DB, Bishop DJ (2018) <doi:10.1371/journal.pone.0199794>. Hofmann P,
Tschakert G (2017) <doi:10.3389/fphys.2017.00337>. Hofmann P, Pokan R, von
Duvillard SP, Seibert FJ, Zweiker R, Schmid P (1997)
<doi:10.1097/00005768-199706000-00005>. Pokan R, Hofmann P, Von Duvillard
SP, et al. (1997) <doi:10.1097/00005768-199708000-00009>. Dickhuth H-H,
Yin L, Niess A, et al. (1999) <doi:10.1055/s-2007-971105>.

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
