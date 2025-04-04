%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatemR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Spatial Autoregresive Models for Mean and Variance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss >= 5.3.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gamlss.dist 
Requires:         R-CRAN-gamlss >= 5.3.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-gamlss.dist 

%description
Modeling spatial dependencies in dependent variables, extending
traditional spatial regression approaches. It allows for the joint
modeling of both the mean and the variance of the dependent variable,
incorporating semiparametric effects in both models. Based on generalized
additive models (GAM), the package enables the inclusion of non-parametric
terms while maintaining the classical theoretical framework of spatial
regression. Additionally, it implements the Generalized Spatial
Autoregression (GSAR) model, which extends classical methods like logistic
Spatial Autoregresive Models (SAR), probit Spatial Autoregresive Models
(SAR), and Poisson Spatial Autoregresive Models (SAR), offering greater
flexibility in modeling spatial dependencies and significantly improving
computational efficiency and the statistical properties of the estimators.
Related work includes: a) J.D. Toloza-Delgado, Melo O.O., Cruz N.A.
(2024). "Joint spatial modeling of mean and non-homogeneous variance
combining semiparametric SAR and GAMLSS models for hedonic prices".
<doi:10.1016/j.spasta.2024.100864>. b) Cruz, N. A., Toloza-Delgado, J. D.,
Melo, O. O. (2024). "Generalized spatial autoregressive model".
<doi:10.48550/arXiv.2412.00945>.

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
