%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bupaverse
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load the 'bupaverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.2.0
BuildRequires:    R-CRAN-magrittr >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 1.0.0
BuildRequires:    R-CRAN-glue >= 1.0.0
BuildRequires:    R-CRAN-edeaR >= 0.9.1
BuildRequires:    R-CRAN-processmapR >= 0.5.2
BuildRequires:    R-CRAN-bupaR >= 0.5.1
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-eventdataR >= 0.3.1
BuildRequires:    R-CRAN-processcheckR >= 0.1.4
Requires:         R-CRAN-cli >= 3.2.0
Requires:         R-CRAN-magrittr >= 2.0.0
Requires:         R-CRAN-rlang >= 1.0.0
Requires:         R-CRAN-glue >= 1.0.0
Requires:         R-CRAN-edeaR >= 0.9.1
Requires:         R-CRAN-processmapR >= 0.5.2
Requires:         R-CRAN-bupaR >= 0.5.1
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-eventdataR >= 0.3.1
Requires:         R-CRAN-processcheckR >= 0.1.4

%description
The 'bupaverse' is an open-source, integrated suite of R-packages for
handling and analysing business process data, developed by the Business
Informatics research group at Hasselt University, Belgium. Profoundly
inspired by the 'tidyverse' package, the 'bupaverse' package is designed
to facilitate the installation and loading of multiple 'bupaverse'
packages in a single step. Learn more about 'bupaverse' at the
<https://bupar.net> homepage.

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
