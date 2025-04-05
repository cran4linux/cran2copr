%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  plm
%global packver   2.6-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6.6
Release:          1%{?dist}%{?buildtag}
Summary:          Linear Models for Panel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-collapse >= 1.8.9
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-bdsmatrix 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-stats 
Requires:         R-CRAN-collapse >= 1.8.9
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-bdsmatrix 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Formula 
Requires:         R-stats 

%description
A set of estimators for models and (robust) covariance matrices, and tests
for panel data econometrics, including within/fixed effects, random
effects, between, first-difference, nested random effects as well as
instrumental-variable (IV) and Hausman-Taylor-style models, panel
generalized method of moments (GMM) and general FGLS models, mean groups
(MG), demeaned MG, and common correlated effects (CCEMG) and pooled (CCEP)
estimators with common factors, variable coefficients and limited
dependent variables models. Test functions include model specification,
serial correlation, cross-sectional dependence, panel unit root and panel
Granger (non-)causality. Typical references are general econometrics text
books such as Baltagi (2021), Econometric Analysis of Panel Data
(<doi:10.1007/978-3-030-53953-5>), Hsiao (2014), Analysis of Panel Data
(<doi:10.1017/CBO9781139839327>), and Croissant and Millo (2018), Panel
Data Econometrics with R (<doi:10.1002/9781119504641>).

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
