%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weibullness
%global packver   1.24.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.24.1
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Test for Weibull Distribution (Weibullness)

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-methods 

%description
Conducts a goodness-of-fit test for the Weibull distribution (referred to
as the weibullness test) and furnishes parameter estimations for both the
two-parameter and three-parameter Weibull distributions. Notably, the
threshold parameter is derived through correlation from the Weibull plot.
Additionally, this package conducts goodness-of-fit assessments for the
exponential, Gumbel, and inverse Weibull distributions, accompanied by
parameter estimations. For more details, see Park (2017)
<doi:10.23055/ijietap.2017.24.4.2848>, Park (2018)
<doi:10.1155/2018/6056975>, and Park (2023) <doi:10.3390/math11143156>.
This work was supported by the National Research Foundation of Korea (NRF)
grants funded by the Korea government (MSIT) (No. 2022R1A2C1091319,
RS-2023-00242528).

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
