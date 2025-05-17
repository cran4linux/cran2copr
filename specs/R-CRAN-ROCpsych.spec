%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ROCpsych
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Compute and Compare Diagnostic Test Statistics Across Groups

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reportROC 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
Requires:         R-CRAN-reportROC 
Requires:         R-CRAN-pROC 
Requires:         R-stats 

%description
Functions for (1) computing diagnostic test statistics (sensitivity,
specificity, etc.) from confusion matrices with adjustment for various
base rates or known prevalence based on McCaffrey et al (2003)
<doi:10.1007/978-1-4615-0079-7_1>, (2) computing optimal cut-off scores
with different criteria including maximizing sensitivity, maximizing
specificity, and maximizing the Youden Index from Youden (1950)
<doi:10.1002/1097-0142(1950)3:1%%3C32::AID-CNCR2820030106%%3E3.0.CO;2-3>,
and (3) displaying and comparing classification statistics and area under
the receiver operating characteristic (ROC) curves or area under the
curves (AUC) across consecutive categories for ordinal variables.

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
