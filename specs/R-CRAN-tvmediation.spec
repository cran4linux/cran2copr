%global packname  tvmediation
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Varying Mediation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats >= 4.0.3
BuildRequires:    R-CRAN-ggplot2 >= 3.3.3
BuildRequires:    R-CRAN-dplyr >= 1.0.4
BuildRequires:    R-CRAN-kedd >= 1.0.3
BuildRequires:    R-CRAN-locpol >= 0.7.0
Requires:         R-stats >= 4.0.3
Requires:         R-CRAN-ggplot2 >= 3.3.3
Requires:         R-CRAN-dplyr >= 1.0.4
Requires:         R-CRAN-kedd >= 1.0.3
Requires:         R-CRAN-locpol >= 0.7.0

%description
Provides functions for estimating mediation effects that vary over time as
described in Cai, X., Piper, M. E., Li, R., & Coffman, D. L. (2020).
Estimation and inference for the mediation effect in a time-varying
mediation model. <arXiv:2008.11797>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
