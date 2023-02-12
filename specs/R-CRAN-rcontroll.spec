%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcontroll
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Individual-Based Forest Growth Simulator 'TROLL'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-lidR >= 4.0.1
BuildRequires:    R-methods >= 3.5.0
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-parallel >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-sys >= 3.2
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-terra >= 1.5.16
BuildRequires:    R-CRAN-foreach >= 1.4.1
BuildRequires:    R-CRAN-readr >= 1.3.0
BuildRequires:    R-CRAN-reshape2 >= 1.3.0
BuildRequires:    R-CRAN-doParallel >= 1.0.7
BuildRequires:    R-CRAN-iterators >= 1.0.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-doSNOW >= 1.0.10
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-gganimate >= 1.0.0
BuildRequires:    R-CRAN-vroom >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-viridis >= 0.4.0
BuildRequires:    R-CRAN-RcppGSL 
Requires:         R-CRAN-lidR >= 4.0.1
Requires:         R-methods >= 3.5.0
Requires:         R-utils >= 3.5.0
Requires:         R-parallel >= 3.5.0
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-sys >= 3.2
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-terra >= 1.5.16
Requires:         R-CRAN-foreach >= 1.4.1
Requires:         R-CRAN-readr >= 1.3.0
Requires:         R-CRAN-reshape2 >= 1.3.0
Requires:         R-CRAN-doParallel >= 1.0.7
Requires:         R-CRAN-iterators >= 1.0.5
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-doSNOW >= 1.0.10
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-gganimate >= 1.0.0
Requires:         R-CRAN-vroom >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-viridis >= 0.4.0

%description
'TROLL' is coded in C++ and it typically simulates hundreds of thousands
of individuals over hundreds of years. The 'rcontroll' R package is a
wrapper of 'TROLL'. 'rcontroll' includes functions that generate inputs
for simulations and run simulations. Finally, it is possible to analyse
the 'TROLL' outputs through tables, figures, and maps taking advantage of
other R visualisation packages. 'rcontroll' also offers the possibility to
generate a virtual LiDAR point cloud that corresponds to a snapshot of the
simulated forest.

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
