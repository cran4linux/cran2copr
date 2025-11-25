%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dcmstan
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generate 'Stan' Code for Diagnostic Classification Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dagitty 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggdag 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rdcmchecks 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dagitty 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggdag 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rdcmchecks 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Diagnostic classification models are psychometric models used to
categorically estimate respondents mastery, or proficiency, on a set of
predefined skills (Bradshaw, 2016, <doi:10.1002/9781118956588.ch13>).
Diagnostic models can be estimated with 'Stan'; however, the necessary
scripts can be long and complicated. This package automates the creation
of 'Stan' scripts for diagnostic classification models. Specify different
types of diagnostic models, define prior distributions, and automatically
generate the necessary 'Stan' code for estimating the model.

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
