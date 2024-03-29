%global __brp_check_rpaths %{nil}
%global packname  CatPredi
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Categorisation of Continuous Variables in Prediction Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-rgenoud 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-rgenoud 
Requires:         R-CRAN-mgcv 
Requires:         R-stats 
Requires:         R-graphics 

%description
Allows the user to categorise a continuous predictor variable in a
logistic or a Cox proportional hazards regression setting, by maximising
the discriminative ability of the model. I Barrio, I Arostegui, MX
Rodriguez-Alvarez, JM Quintana (2015) <doi:10.1177/0962280215601873>. I
Barrio, MX Rodriguez-Alvarez, L Meira-Machado, C Esteban, I Arostegui
(2017) <https://www.idescat.cat/sort/sort411/41.1.3.barrio-etal.pdf>.

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
