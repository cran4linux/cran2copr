%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ct
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Integrated Camera-Trap Data Management and Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-cli >= 3.6.3
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-Distance >= 2.0.0
BuildRequires:    R-CRAN-terra >= 1.8.29
BuildRequires:    R-CRAN-activity >= 1.3.4
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-rlang >= 1.1.5
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-sf >= 1.0.19
BuildRequires:    R-CRAN-Rcpp >= 1.0.14
BuildRequires:    R-CRAN-overlap >= 0.3.9
BuildRequires:    R-CRAN-sbd >= 0.1.0
BuildRequires:    R-CRAN-camtrapdp 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-cli >= 3.6.3
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-Distance >= 2.0.0
Requires:         R-CRAN-terra >= 1.8.29
Requires:         R-CRAN-activity >= 1.3.4
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-rlang >= 1.1.5
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-sf >= 1.0.19
Requires:         R-CRAN-Rcpp >= 1.0.14
Requires:         R-CRAN-overlap >= 0.3.9
Requires:         R-CRAN-sbd >= 0.1.0
Requires:         R-CRAN-camtrapdp 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 

%description
An integrated, tidyverse-friendly workflow for camera trap data in
wildlife monitoring and ecological research. Reads and edits media
metadata, filters independent detections, analyses activity patterns and
species diversity, and estimates species density or abundance with several
methods, including the random encounter model, camera-trap distance
sampling, time-to-event, space-to-event, and the random encounter and
staying-time model (see Rowcliffe et al. (2008)
<doi:10.1111/j.1365-2664.2008.01473.x>, Howe et al. (2017)
<doi:10.1111/2041-210X.12790>, Nakashima et al. (2018)
<doi:10.1111/1365-2664.13059>, and Moeller et al. (2018)
<doi:10.1002/ecs2.2331>).

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
