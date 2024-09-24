%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurvMA
%global packver   1.6.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.8
Release:          1%{?dist}%{?buildtag}
Summary:          Model Averaging Prediction of Personalized Survival Probabilities

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-pec 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-pec 
Requires:         R-CRAN-quadprog 
Requires:         R-splines 
Requires:         R-methods 

%description
Provide model averaging-based approaches that can be used to predict
personalized survival probabilities. The key underlying idea is to
approximate the conditional survival function using a weighted average of
multiple candidate models. Two scenarios of candidate models are allowed:
(Scenario 1) partial linear Cox model and (Scenario 2) time-varying
coefficient Cox model. A reference of the underlying methods is Li and
Wang (2023) <doi:10.1016/j.csda.2023.107759>.

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
