%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  janus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Optimized Recommending System Based on 'tensorflow'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-keras >= 2.9.0
BuildRequires:    R-CRAN-tensorflow >= 2.9.0
BuildRequires:    R-CRAN-RcppAlgos >= 2.6.0
BuildRequires:    R-CRAN-hash >= 2.2.6.2
BuildRequires:    R-CRAN-readr >= 2.1.2
BuildRequires:    R-CRAN-lubridate >= 1.7.10
BuildRequires:    R-CRAN-reticulate >= 1.26
BuildRequires:    R-CRAN-dplyr >= 1.0.10
BuildRequires:    R-CRAN-tictoc >= 1.0
BuildRequires:    R-CRAN-Rmpfr >= 0.8.7
BuildRequires:    R-CRAN-forcats >= 0.5.1
BuildRequires:    R-CRAN-narray >= 0.4.1.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-Metrics >= 0.1.4
BuildRequires:    R-CRAN-StatRank >= 0.0.6
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-keras >= 2.9.0
Requires:         R-CRAN-tensorflow >= 2.9.0
Requires:         R-CRAN-RcppAlgos >= 2.6.0
Requires:         R-CRAN-hash >= 2.2.6.2
Requires:         R-CRAN-readr >= 2.1.2
Requires:         R-CRAN-lubridate >= 1.7.10
Requires:         R-CRAN-reticulate >= 1.26
Requires:         R-CRAN-dplyr >= 1.0.10
Requires:         R-CRAN-tictoc >= 1.0
Requires:         R-CRAN-Rmpfr >= 0.8.7
Requires:         R-CRAN-forcats >= 0.5.1
Requires:         R-CRAN-narray >= 0.4.1.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-Metrics >= 0.1.4
Requires:         R-CRAN-StatRank >= 0.0.6

%description
Proposes a coarse-to-fine optimization of a recommending system based on
deep-neural networks using 'tensorflow'.

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
