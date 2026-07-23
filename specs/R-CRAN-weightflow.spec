%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  weightflow
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Declarative API for Staged Survey Weights

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Builds survey weights from design base weights by chaining hierarchical
adjustments (unknown eligibility, nonresponse and calibration) through a
declarative, pipeable, 'tidymodels'-style API. Calibration follows Deville
and Sarndal (1992) <doi:10.2307/2290268>. Variances are obtained with a
bootstrap that resamples primary sampling units and re-applies the whole
recipe on each replicate, following the rescaling bootstrap of Rao and Wu
(1988) <doi:10.1080/01621459.1988.10478591>, so the replicate weights
carry the variability of every adjustment. The weights also bridge to the
'survey' and 'srvyr' packages for design-based inference.

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
