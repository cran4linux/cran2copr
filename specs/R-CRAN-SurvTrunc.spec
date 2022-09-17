%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurvTrunc
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Doubly Truncated Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Package performs Cox regression and survival distribution function
estimation when the survival times are subject to double truncation. In
case that the survival and truncation times are quasi-independent, the
estimation procedure for each method involves inverse probability
weighting, where the weights correspond to the inverse of the selection
probabilities and are estimated using the survival times and truncation
times only. A test for checking this independence assumption is also
included in this package. The functions available in this package for Cox
regression, survival distribution function estimation, and testing
independence under double truncation are based on the following methods,
respectively: Rennert and Xie (2018) <doi:10.1111/biom.12809>, Shen (2010)
<doi:10.1007/s10463-008-0192-2>, Martin and Betensky (2005)
<doi:10.1198/016214504000001538>. When the survival times are dependent on
at least one of the truncation times, an EM algorithm is employed to
obtain point estimates for the regression coefficients. The standard
errors are calculated using the bootstrap method. See Rennert and Xie
(2022) <doi:10.1111/biom.13451>. Both the independent and dependent cases
assume no censoring is present in the data. Please contact Lior Rennert
<liorr@clemson.edu> for questions regarding function coxDT and Yidan Shi
<yidan.shi@pennmedicine.upenn.edu> for questions regarding function
coxDTdep.

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
