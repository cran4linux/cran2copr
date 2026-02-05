%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PanelTM
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two- And Three-Way Dynamic Panel Threshold Regression Model for Change Point Detection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-MASS 

%description
Estimation of two- and three-way dynamic panel threshold regression models
(Di Lascio and Perazzini (2024) <https://repec.unibz.it/bemps104.pdf>; Di
Lascio and Perazzini (2022, ISBN:978-88-9193-231-0); Seo and Shin (2016)
<doi:10.1016/j.jeconom.2016.03.005>) through the generalized method of
moments based on the first difference transformation and the use of
instrumental variables. The models can be used to find a change point
detection in the time series. In addition, random number generation is
also implemented.

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
