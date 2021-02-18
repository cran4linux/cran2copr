%global packname  ROCket
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple and Fast ROC Curves

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.13.0
Requires:         R-CRAN-data.table >= 1.13.0

%description
A set of functions for receiver operating characteristic (ROC) curve
estimation and area under the curve (AUC) calculation. All functions are
designed to work with aggregated data; nevertheless, they can also handle
raw samples. In 'ROCket', we distinguish two types of ROC curve
representations: 1) parametric curves - the true positive rate (TPR) and
the false positive rate (FPR) are functions of a parameter (the score), 2)
functions - TPR is a function of FPR. There are several ROC curve
estimation methods available. An introduction to the mathematical
background of the implemented methods (and much more) can be found in de
Zea Bermudez, Gonçalves, Oliveira & Subtil (2014)
<https://www.ine.pt/revstat/pdf/rs140101.pdf> and Cai & Pepe (2004)
<doi:10.1111/j.0006-341X.2004.00200.x>.

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
