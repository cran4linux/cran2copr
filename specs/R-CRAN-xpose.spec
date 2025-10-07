%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  xpose
%global packver   0.4.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.21
Release:          1%{?dist}%{?buildtag}
Summary:          Diagnostics for Pharmacometric Models

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.2
BuildRequires:    R-CRAN-tibble >= 3.3.0
BuildRequires:    R-CRAN-readr >= 2.1.5
BuildRequires:    R-CRAN-stringr >= 1.5.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-vpc >= 1.2.2
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-ggforce >= 0.5.0
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.5.2
Requires:         R-CRAN-tibble >= 3.3.0
Requires:         R-CRAN-readr >= 2.1.5
Requires:         R-CRAN-stringr >= 1.5.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-vpc >= 1.2.2
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-ggforce >= 0.5.0
Requires:         R-utils 
Requires:         R-stats 

%description
Diagnostics for non-linear mixed-effects (population) models from 'NONMEM'
<https://www.iconplc.com/solutions/technologies/nonmem/>. 'xpose'
facilitates data import, creation of numerical run summary and provide
'ggplot2'-based graphics for data exploration and model diagnostics.

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
