%global __brp_check_rpaths %{nil}
%global packname  MLFS
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Forest Simulator

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-pscl >= 1.5.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-tidyr >= 1.1.3
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-naivebayes >= 0.9.7
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-brnn >= 0.6
BuildRequires:    R-CRAN-ranger >= 0.13.1
Requires:         R-CRAN-pscl >= 1.5.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-tidyr >= 1.1.3
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-naivebayes >= 0.9.7
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-brnn >= 0.6
Requires:         R-CRAN-ranger >= 0.13.1

%description
Climate-sensitive forest simulator based on the principles of machine
learning. It stimulates all key processes in the forest: radial growth,
height growth, mortality, crown recession, regeneration and harvesting.
The method for predicting tree heights was described by Skudnik and
Jevšenak (2022) <doi:10.1016/j.foreco.2022.120017>, while the method for
predicting basal area increments (BAI) was described by Jevšenak and
Skudnik (2021) <doi:10.1016/j.foreco.2020.118601>.

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
