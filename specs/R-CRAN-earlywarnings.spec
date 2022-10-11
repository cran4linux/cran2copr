%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  earlywarnings
%global packver   1.1.29
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.29
Release:          1%{?dist}%{?buildtag}
Summary:          Early Warning Signals for Critical Transitions in Time Series

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-tgp 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-tgp 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-nortest 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-KernSmooth 
Requires:         R-methods 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-som 
Requires:         R-CRAN-spam 
Requires:         R-stats 
Requires:         R-CRAN-knitr 

%description
The Early-Warning-Signals Toolbox provides methods for estimating
statistical changes in time series that can be used for identifying nearby
critical transitions.

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
