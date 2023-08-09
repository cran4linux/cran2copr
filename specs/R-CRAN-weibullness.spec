%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weibullness
%global packver   1.23.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.23.8
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Test for Weibull Distribution (Weibullness)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Performs a goodness-of-fit test for Weibull distribution (weibullness
test) and provides the parameter estimates of the two- and three-parameter
Weibull distributions. Note that the threshold parameter is estimated
based on the correlation from the Weibull plot. For more details, see
<doi:10.23055/ijietap.2017.24.4.2848>, <doi:10.1155/2018/6056975>, and
<doi:10.3390/math11143156>. This work was supported by the National
Research Foundation of Korea (NRF) grant funded by the Korea government
(MSIT) (No. 2022R1A2C1091319, RS-2023-00242528).

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
