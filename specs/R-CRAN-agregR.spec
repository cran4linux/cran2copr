%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agregR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian State-Space Aggregation of Brazilian Presidential Polls

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggdist >= 3.1.0
BuildRequires:    R-CRAN-instantiate 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-systemfonts 
Requires:         R-CRAN-ggdist >= 3.1.0
Requires:         R-CRAN-instantiate 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-stringi 
Requires:         R-grid 
Requires:         R-CRAN-systemfonts 

%description
A set of dynamic measurement models to estimate latent vote shares from
noisy polling sources. The models build on Jackman (2009, ISBN:
9780470011546) and feature specialized methods for bias adjustment based
on past performance and correction for asymmetric errors based on
candidate political alignment.

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
