%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svyROC
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the ROC Curve and the AUC for Complex Survey Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-svyVarSel 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-svyVarSel 

%description
Estimate the receiver operating characteristic (ROC) curve, area under the
curve (AUC) and optimal cut-off points for individual classification
taking into account complex sampling designs when working with complex
survey data. Methods implemented in this package are described in: A.
Iparragirre, I. Barrio, I. Arostegui (2024) <doi:10.1002/sta4.635>; A.
Iparragirre, I. Barrio, J. Aramendi, I. Arostegui (2022)
<doi:10.2436/20.8080.02.121>; A. Iparragirre, I. Barrio (2024)
<doi:10.1007/978-3-031-65723-8_7>.

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
