%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ISEtools
%global packver   3.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ion Selective Electrodes Analysis Methods

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-coda 

%description
Characterisation and calibration of single or multiple Ion Selective
Electrodes (ISEs); activity estimation of experimental samples. Implements
methods described in: Dillingham, P.W., Radu, T., Diamond, D., Radu, A.
and McGraw, C.M. (2012) <doi:10.1002/elan.201100510>, Dillingham, P.W.,
Alsaedi, B.S.O. and McGraw, C.M. (2017) <doi:10.1109/ICSENS.2017.8233898>,
Dillingham, P.W., Alsaedi, B.S.O., Radu, A., and McGraw, C.M. (2019)
<doi:10.3390/s19204544>, and Dillingham, P.W., Alsaedi, B.S.O.,
Granados-Focil, S., Radu, A., and McGraw, C.M. (2020)
<doi:10.1021/acssensors.9b02133>.

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
