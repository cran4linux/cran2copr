%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plutor
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Useful Functions for Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-baizer 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggh4x 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggsci 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-repr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-baizer 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggh4x 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggsci 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-repr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
In ancient Roman mythology, 'Pluto' was the ruler of the underworld and
presides over the afterlife. 'Pluto' was frequently conflated with
'Plutus', the god of wealth, because mineral wealth was found underground.
When plotting with R, you try once, twice, practice again and again, and
finally you get a pretty figure you want. It's a 'plot tour', a tour about
repetition and reward. Hope 'plutor' helps you on the tour!

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
