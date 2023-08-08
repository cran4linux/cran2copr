%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rspiro
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Implementation of Spirometry Equations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Implementation of various spirometry equations in R, currently the
GLI-2012 (Global Lung Initiative; Quanjer et al. 2012
<doi:10.1183/09031936.00080312>), the race-neutral GLI global 2022 (Global
Lung Initiative; Bowerman et al. 2023 <doi:10.1164/rccm.202205-0963OC>)
and the NHANES3 (National Health and Nutrition Examination Survey;
Hankinson et al. 1999 <doi:10.1164/ajrccm.159.1.9712108>) equations.
Contains user-friendly functions to calculate predicted and LLN (Lower
Limit of Normal) values for different spirometric parameters such as FEV1
(Forced Expiratory Volume in 1 second), FVC (Forced Vital Capacity), etc,
and to convert absolute spirometry measurements to percent (%%) predicted
and z-scores.

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
