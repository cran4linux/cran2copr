%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rr2
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R2s for Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-phylolm >= 2.6.2
BuildRequires:    R-CRAN-phyr >= 1.0.3
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-nlme 
Requires:         R-CRAN-phylolm >= 2.6.2
Requires:         R-CRAN-phyr >= 1.0.3
Requires:         R-stats 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-ape 
Requires:         R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-nlme 

%description
Three methods to calculate R2 for models with correlated errors, including
Phylogenetic GLS, Phylogenetic Logistic Regression, Linear Mixed Models
(LMMs), and Generalized Linear Mixed Models (GLMMs). See details in Ives
2018 <doi:10.1093/sysbio/syy060>.

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
