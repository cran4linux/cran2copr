%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rmpw
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Mediation Analysis Using Weighting Approach

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-MASS 

%description
We implement causal mediation analysis using the methods proposed by Hong
(2010) and Hong, Deutsch & Hill (2015) <doi:10.3102/1076998615583902>. It
allows the estimation and hypothesis testing of causal mediation effects
through ratio of mediator probability weights (RMPW). This strategy
conveniently relaxes the assumption of no treatment-by-mediator
interaction while greatly simplifying the outcome model specification
without invoking strong distributional assumptions. We also implement a
sensitivity analysis by extending the RMPW method to assess potential bias
in the presence of omitted pretreatment or posttreatment covariates. The
sensitivity analysis strategy was proposed by Hong, Qin, and Yang (2018)
<doi:10.3102/1076998617749561>.

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
