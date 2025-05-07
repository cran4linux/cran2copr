%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MEAanalysis
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse and Visualise Multi Electrode Array Burst Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-janitor >= 2.2.0
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-tidyverse >= 2.0.0
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-knitr >= 1.46
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-readxl >= 1.4.3
BuildRequires:    R-CRAN-kableExtra >= 1.4.0
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-data.table >= 1.15.4
BuildRequires:    R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-janitor >= 2.2.0
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-tidyverse >= 2.0.0
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-knitr >= 1.46
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-readxl >= 1.4.3
Requires:         R-CRAN-kableExtra >= 1.4.0
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-data.table >= 1.15.4
Requires:         R-CRAN-dplyr >= 1.1.4

%description
Analyse and visualise multi electrode array data at the single electrode
and whole well level, downstream of 'AxIS Navigator 3.6.2 Software'
processing. Compare bursting parameters between time intervals and
recordings using the bar chart visualisation functions. Compatible with
12- and 24- well plates.

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
