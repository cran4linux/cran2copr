%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  betaselectr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Betas-Select in Structural Equation Models and Linear Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-manymome 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-lavaan.printer 
Requires:         R-CRAN-boot 
Requires:         R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-manymome 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-lavaan.printer 

%description
It computes betas-select, coefficients after standardization in structural
equation models and regression models, standardizing only selected
variables. Supports models with moderation, with product terms formed
after standardization. It also offers confidence intervals that account
for standardization, including bootstrap confidence intervals as proposed
by Cheung et al. (2022) <doi:10.1037/hea0001188>.

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
