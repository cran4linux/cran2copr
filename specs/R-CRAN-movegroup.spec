%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  movegroup
%global packver   2024.03.05
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2024.03.05
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing and Quantifying Space Use Data for Groups of Animals

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-move >= 4.1.6
BuildRequires:    R-CRAN-raster >= 3.5.15
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-ggmap >= 3.0.0
BuildRequires:    R-CRAN-magick >= 2.8.2
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-terra >= 1.7.39
BuildRequires:    R-CRAN-knitr >= 1.45
BuildRequires:    R-CRAN-sp >= 1.4.6
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-beepr >= 1.3
BuildRequires:    R-CRAN-tidyr >= 1.2.0
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-sf >= 1.0.7
BuildRequires:    R-CRAN-purrr >= 1.0.2
BuildRequires:    R-CRAN-rlang >= 1.0.2
BuildRequires:    R-CRAN-viridis >= 0.6.4
BuildRequires:    R-CRAN-stars >= 0.5.5
BuildRequires:    R-CRAN-starsExtra >= 0.2.7
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-move >= 4.1.6
Requires:         R-CRAN-raster >= 3.5.15
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-ggmap >= 3.0.0
Requires:         R-CRAN-magick >= 2.8.2
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-terra >= 1.7.39
Requires:         R-CRAN-knitr >= 1.45
Requires:         R-CRAN-sp >= 1.4.6
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-beepr >= 1.3
Requires:         R-CRAN-tidyr >= 1.2.0
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-sf >= 1.0.7
Requires:         R-CRAN-purrr >= 1.0.2
Requires:         R-CRAN-rlang >= 1.0.2
Requires:         R-CRAN-viridis >= 0.6.4
Requires:         R-CRAN-stars >= 0.5.5
Requires:         R-CRAN-starsExtra >= 0.2.7
Requires:         R-utils 
Requires:         R-methods 

%description
Offers an easy and automated way to scale up individual-level space use
analysis to that of groups. Contains a function from the 'move' package to
calculate a dynamic Brownian bridge movement model from movement data for
individual animals, as well as functions to visualize and quantify space
use for individuals aggregated in groups. Originally written with passive
acoustic telemetry in mind, this package also provides functionality to
account for unbalanced acoustic receiver array designs, and satellite tag
data.

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
