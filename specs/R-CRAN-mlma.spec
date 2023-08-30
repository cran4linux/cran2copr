%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlma
%global packver   6.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multilevel Mediation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.1
Requires:         R-core >= 2.14.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coxme 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-splines 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-car 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coxme 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-survival 
Requires:         R-splines 

%description
Do multilevel mediation analysis with generalized additive multilevel
models. The analysis method is described in Yu and Li (2020),
"Third-Variable Effect Analysis with Multilevel Additive Models", PLoS ONE
15(10): e0241072.

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
