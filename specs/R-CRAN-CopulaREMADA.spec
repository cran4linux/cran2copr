%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CopulaREMADA
%global packver   1.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Mixed Models for Multivariate Meta-Analysis of Diagnostic Test Accuracy Studies

License:          GPL (>= 3.5.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-matlab 
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-mc2d 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-matlab 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-mc2d 

%description
The bivariate copula mixed model for meta-analysis of diagnostic test
accuracy studies in Nikoloulopoulos (2015) <doi:10.1002/sim.6595> and
Nikoloulopoulos (2018) <doi:10.1007/s10182-017-0299-y>. The vine copula
mixed model for meta-analysis of diagnostic test accuracy studies
accounting for disease prevalence in Nikoloulopoulos (2017)
<doi:10.1177/0962280215596769> and also accounting for non-evaluable
subjects in Nikoloulopoulos (2020) <doi:10.1515/ijb-2019-0107>. The hybrid
vine copula mixed model for meta-analysis of diagnostic test accuracy
case-control and cohort studies in Nikoloulopoulos (2018)
<doi:10.1177/0962280216682376>. The D-vine copula mixed model for
meta-analysis and comparison of two diagnostic tests in Nikoloulopoulos
(2019) <doi:10.1177/0962280218796685>. The multinomial quadrivariate
D-vine copula mixed model for meta-analysis of diagnostic tests with
non-evaluable subjects in Nikoloulopoulos (2020)
<doi:10.1177/0962280220913898>. The one-factor copula mixed model for
joint meta-analysis of multiple diagnostic tests in Nikoloulopoulos (2022)
<doi:10.1111/rssa.12838>. The multinomial six-variate 1-truncated D-vine
copula mixed model for meta-analysis of two diagnostic tests accounting
for within and between studies dependence in Nikoloulopoulos (2024)
<doi:10.1177/09622802241269645>. The 1-truncated D-vine copula mixed
models for meta-analysis of diagnostic accuracy studies without a gold
standard (Nikoloulopoulos, 2024).

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
