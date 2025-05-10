%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CvmortalityMult
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cross-Validation for Multi-Population Mortality Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm >= 1.1.2
BuildRequires:    R-CRAN-StMoMo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-tmap 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-graphics 
Requires:         R-CRAN-gnm >= 1.1.2
Requires:         R-CRAN-StMoMo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-tmap 
Requires:         R-CRAN-sf 
Requires:         R-graphics 

%description
Implementation of cross-validation method for testing the forecasting
accuracy of several multi-population mortality models. The family of
multi-population includes several multi-population mortality models
proposed through the actuarial and demography literature. The package
includes functions for fitting and forecast the mortality rates of several
populations. Additionally, we include functions for testing the
forecasting accuracy of different multi-population models. References.
Atance, D., Debon, A., and Navarro, E. (2020) <doi:10.3390/math8091550>.
Bergmeir, C. & Benitez, J.M. (2012) <doi:10.1016/j.ins.2011.12.028>.
Debon, A., Montes, F., & Martinez-Ruiz, F. (2011)
<doi:10.1007/s13385-011-0043-z>. Lee, R.D. & Carter, L.R. (1992)
<doi:10.1080/01621459.1992.10475265>. Russolillo, M., Giordano, G., &
Haberman, S. (2011) <doi:10.1080/03461231003611933>. Santolino, M. (2023)
<doi:10.3390/risks11100170>.

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
