%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pk4adi
%global packver   0.1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          PK for Anesthetic Depth Indicators

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-stats 

%description
Calculate and compare the prediction probability (PK) values for
Anesthetic Depth Indicators. The PK values are widely used for measuring
the performance of anesthetic depth and were first proposed by the group
of Dr. Warren D. Smith in the paper Warren D. Smith; Robert C. Dutton; Ty
N. Smith (1996) <doi:10.1097/00000542-199601000-00005> and Warren D.
Smith; Robert C. Dutton; Ty N. Smith (1996)
<doi:10.1002/(SICI)1097-0258(19960615)15:11%%3C1199::AID-SIM218%%3E3.0.CO;2-Y>.
The authors provided two 'Microsoft Excel' files in xls format for
calculating and comparing PK values. This package provides an easy-to-use
API for calculating and comparing PK values in R.

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
