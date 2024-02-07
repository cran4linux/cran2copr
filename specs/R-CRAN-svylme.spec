%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  svylme
%global packver   1.5-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Mixed Models for Complex Survey Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Linear mixed models for complex survey data, by pairwise composite
likelihood, as described in Lumley & Huang (2023) <arXiv:2311.13048>.
Supports nested and crossed random effects, and correlated random effects
as in genetic models.  Allows for multistage sampling and for other
designs where pairwise sampling probabilities are specified or can be
calculated.

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
