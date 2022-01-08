%global __brp_check_rpaths %{nil}
%global packname  tidybayes
%global packver   3.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Data and 'Geoms' for Bayesian Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-ggdist >= 3.0.0
BuildRequires:    R-CRAN-posterior >= 1.0.1
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-rlang >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-arrayhelpers 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-ggdist >= 3.0.0
Requires:         R-CRAN-posterior >= 1.0.1
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-rlang >= 0.3.0
Requires:         R-methods 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-arrayhelpers 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-vctrs 

%description
Compose data for and extract, manipulate, and visualize posterior draws
from Bayesian models ('JAGS', 'Stan', 'rstanarm', 'brms', 'MCMCglmm',
'coda', ...) in a tidy data format. Functions are provided to help extract
tidy data frames of draws from Bayesian models and that generate point
summaries and intervals in a tidy format. In addition, 'ggplot2' 'geoms'
and 'stats' are provided for common visualization primitives like points
with multiple uncertainty intervals, eye plots (intervals plus densities),
and fit curves with multiple, arbitrary uncertainty bands.

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
