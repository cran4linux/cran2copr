%global __brp_check_rpaths %{nil}
%global packname  BayesSampling
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayes Linear Estimators for Finite Population

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-matrixcalc 

%description
Allows the user to apply the Bayes Linear approach to finite population
with the Simple Random Sampling - BLE_SRS() - and the Stratified Simple
Random Sampling design - BLE_SSRS() - (both without replacement), to the
Ratio estimator (using auxiliary information) - BLE_Ratio() - and to
categorical data - BLE_Categorical(). The Bayes linear estimation approach
is applied to a general linear regression model for finite population
prediction in BLE_Reg() and it is also possible to achieve the design
based estimators using vague prior distributions. Based on Gonçalves,
K.C.M, Moura, F.A.S and Migon, H.S.(2014)
<https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X201400111886>.

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
