%global __brp_check_rpaths %{nil}
%global packname  theft
%global packver   0.3.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Handling Extraction of Features from Time Series

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tsibble 
BuildRequires:    R-CRAN-fabletools 
BuildRequires:    R-CRAN-tsfeatures 
BuildRequires:    R-CRAN-feasts 
BuildRequires:    R-CRAN-Rcatch22 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-R.matlab 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-janitor 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tsibble 
Requires:         R-CRAN-fabletools 
Requires:         R-CRAN-tsfeatures 
Requires:         R-CRAN-feasts 
Requires:         R-CRAN-Rcatch22 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-R.matlab 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-janitor 

%description
Consolidates and calculates different sets of time-series features from
multiple 'R' and 'Python' packages including 'Rcatch22' Henderson, T.
(2021) <doi:10.5281/zenodo.5546815>, 'feasts' O'Hara-Wild, M., Hyndman,
R., and Wang, E. (2021) <https://CRAN.R-project.org/package=feasts>,
'tsfeatures' Hyndman, R., Kang, Y., Montero-Manso, P., Talagala, T., Wang,
E., Yang, Y., and O'Hara-Wild, M. (2020)
<https://CRAN.R-project.org/package=tsfeatures>, 'tsfresh' Christ, M.,
Braun, N., Neuffer, J., and Kempa-Liehr A.W. (2018)
<doi:10.1016/j.neucom.2018.03.067>, 'TSFEL' Barandas, M., et al. (2020)
<doi:10.1016/j.softx.2020.100456>, and 'Kats' Facebook Infrastructure Data
Science (2021) <https://facebookresearch.github.io/Kats/>. Provides a
standardised workflow from feature calculation to feature processing,
machine learning classification procedures, and the production of
statistical graphics.

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
