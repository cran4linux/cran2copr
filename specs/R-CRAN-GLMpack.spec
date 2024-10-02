%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GLMpack
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data and Code to Accompany Generalized Linear Models, 2nd Edition

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pBrackets 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-effects 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-censReg 
BuildRequires:    R-CRAN-plm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pBrackets 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-effects 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-censReg 
Requires:         R-CRAN-plm 

%description
Contains all the data and functions used in Generalized Linear Models, 2nd
edition, by Jeff Gill and Michelle Torres. Examples to create all models,
tables, and plots are included for each data set.

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
