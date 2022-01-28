%global __brp_check_rpaths %{nil}
%global packname  GREENeR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geospatial Regression Equation for European Nutrient Losses (GREEN)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.6.1
BuildRequires:    R-grDevices >= 3.5
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-tmap >= 3.3.2
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-magrittr >= 2.0.1
BuildRequires:    R-CRAN-reshape2 >= 1.4.4
BuildRequires:    R-CRAN-parallelly >= 1.30.0
BuildRequires:    R-CRAN-FME >= 1.3.6.1
BuildRequires:    R-CRAN-data.table >= 1.13.6
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.7
BuildRequires:    R-CRAN-sf >= 1.0.2
BuildRequires:    R-CRAN-classInt >= 0.4.3
BuildRequires:    R-CRAN-hydroGOF >= 0.4.0
BuildRequires:    R-CRAN-networkD3 >= 0.4
Requires:         R-graphics >= 3.6.1
Requires:         R-grDevices >= 3.5
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-tmap >= 3.3.2
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-magrittr >= 2.0.1
Requires:         R-CRAN-reshape2 >= 1.4.4
Requires:         R-CRAN-parallelly >= 1.30.0
Requires:         R-CRAN-FME >= 1.3.6.1
Requires:         R-CRAN-data.table >= 1.13.6
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.7
Requires:         R-CRAN-sf >= 1.0.2
Requires:         R-CRAN-classInt >= 0.4.3
Requires:         R-CRAN-hydroGOF >= 0.4.0
Requires:         R-CRAN-networkD3 >= 0.4

%description
Tools and methods to apply the model Geospatial Regression Equation for
European Nutrient losses (GREEN); Grizzetti et al. (2005)
<doi:10.1016/j.jhydrol.2004.07.036>; Grizzetti et al. (2008); Grizzetti et
al. (2012) <doi:10.1111/j.1365-2486.2011.02576.x>; Grizzetti et al. (2021)
<doi:10.1016/j.gloenvcha.2021.102281>.

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
