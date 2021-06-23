%global __brp_check_rpaths %{nil}
%global packname  geoSAE
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geoadditive Small Area Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 
Requires:         R-stats 

%description
This function is an extension of the Small Area Estimation (SAE) model.
Geoadditive Small Area Model is a combination of the geoadditive model
with the Small Area Estimation (SAE) model, by adding geospatial
information to the SAE model. This package refers to J.N.K Rao and Isabel
Molina (2015, ISBN: 978-1-118-73578-7), Bocci, C., & Petrucci, A.
(2016)<doi:10.1002/9781118814963.ch13>, and Ardiansyah, M., Djuraidah, A.,
& Kurnia, A. (2018)<doi:10.21082/jpptp.v2n2.2018.p101-110>.

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
