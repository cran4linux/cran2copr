%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  crumble
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible and General Mediation Analysis Using Riesz Representers

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ife >= 0.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-Rsymphony 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-S7 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-lmtp 
BuildRequires:    R-CRAN-mlr3superlearner 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-ife >= 0.1.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-Rsymphony 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-S7 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-lmtp 
Requires:         R-CRAN-mlr3superlearner 
Requires:         R-CRAN-progressr 

%description
Implements a modern, unified estimation strategy for common mediation
estimands (natural effects, organic effects, interventional effects, and
recanting twins) in combination with modified treatment policies as
described in Liu, Williams, Rudolph, and Díaz (2024)
<doi:10.48550/arXiv.2408.14620>. Estimation makes use of recent
advancements in Riesz-learning to estimate a set of required nuisance
parameters with deep learning. The result is the capability to estimate
mediation effects with binary, categorical, continuous, or multivariate
exposures with high-dimensional mediators and mediator-outcome confounders
using machine learning.

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
