%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bodycompref
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reference Values for CT-Assessed Body Composition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sae 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-gamlss 
Requires:         R-stats 
Requires:         R-CRAN-sae 

%description
Get z-scores, percentiles, absolute values, and percent of predicted of a
reference cohort. Functionality requires installing the data packages
'adiposerefdata' and 'musclerefdata'. For more information on the
underlying research, please visit our website which also includes a
graphical interface. The models and underlying data are described in
Marquardt JP et al.(planned publication 2025; reserved doi
10.1097/RLI.0000000000001104), "Subcutaneous and Visceral adipose tissue
Reference Values from Framingham Heart Study Thoracic and Abdominal CT",
*Investigative Radiology* and Tonnesen PE et al. (2023), "Muscle Reference
Values from Thoracic and Abdominal CT for Sarcopenia Assessment [column]
The Framingham Heart Study", *Investigative Radiology*,
<doi:10.1097/RLI.0000000000001012>.

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
