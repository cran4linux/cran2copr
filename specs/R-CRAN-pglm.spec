%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pglm
%global packver   0.2-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Panel Generalized Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-Formula 

%description
Estimation of panel models for glm-like models: this includes binomial
models (logit and probit), count models (poisson and negbin) and ordered
models (logit and probit), as described in: Baltagi (2013) Econometric
Analysis of Panel Data, ISBN-13:978-1-118-67232-7, Hsiao (2014) Analysis
of Panel Data <doi:10.1017/CBO9781139839327> and Croissant and Millo
(2018), Panel Data Econometrics with R, ISBN:978-1-118-94918-4.

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
