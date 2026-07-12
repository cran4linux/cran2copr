%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pft
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Pulmonary Function Test Interpretation per ERS/ATS 2022

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Computes predicted values and lower/upper limits of normal for pulmonary
function tests according to American Thoracic Society ('ATS') and European
Respiratory Society ('ERS') reference standards. Supports spirometry
(Global Lung Function Initiative 'GLI' 2012, Quanjer et al. (2012)
<doi:10.1183/09031936.00080312>; and the race-neutral 'GLI' 2022 / 'GLI
Global' equations, Bowerman et al. (2023)
<doi:10.1164/rccm.202205-0963OC>), static lung volumes ('GLI' 2021, Hall
et al. (2021) <doi:10.1183/13993003.00289-2020>), and the carbon monoxide
transfer factor / diffusion capacity ('GLI' 2017, Stanojevic et al. (2017)
<doi:10.1183/13993003.00010-2017>, including the 2020 author correction
<doi:10.1183/13993003.50010-2017>). Also assigns interpretive pattern
labels (Normal, Non-specific, Obstructed, Restricted, Mixed) from
spirometry and lung-volume measurements following the 'ERS'/'ATS' 2022
interpretation algorithm, Stanojevic et al. (2022)
<doi:10.1183/13993003.01499-2021>.

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
