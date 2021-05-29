%global packname  multisite.accuracy
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Accuracy in Multisite Machine-Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AROC 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmerTest 
BuildRequires:    R-CRAN-logistf 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-AROC 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmerTest 
Requires:         R-CRAN-logistf 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-survival 

%description
The effects of the site may severely bias the accuracy of a multisite
machine-learning model, even if the analysts removed them when fitting the
model in the 'training set' and when applying the model in the 'test set'.
This simple R package estimates the accuracy of a multisite
machine-learning model unbiasedly as described in (Solanes et al,
Psychiatry Research: Neuroimaging 2021, in Press). It currently supports
the estimation of sensitivity, specificity, balanced accuracy, the area
under the curve, correlation, mean squarer error, and hazard ratio for
binomial, gaussian, and survival (time-to-event) outcomes.

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
