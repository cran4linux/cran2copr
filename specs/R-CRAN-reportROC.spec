%global __brp_check_rpaths %{nil}
%global packname  reportROC
%global packver   3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6
Release:          1%{?dist}%{?buildtag}
Summary:          An Easy Way to Report ROC Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-vcd 
BuildRequires:    R-methods 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-vcd 
Requires:         R-methods 

%description
Provides an easy way to report the results of ROC analysis, including: 1.
an ROC curve. 2. the value of Cutoff, AUC (Area Under Curve), ACC
(accuracy), SEN (sensitivity), SPE (specificity), PLR (positive likelihood
ratio), NLR (negative likelihood ratio), PPV (positive predictive value),
NPV (negative predictive value), PPA (percentage of positive accordance),
NPA (percentage of negative accordance), TPA (percentage of total
accordance), KAPPA (kappa value).

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
