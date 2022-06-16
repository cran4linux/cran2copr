%global __brp_check_rpaths %{nil}
%global packname  lmeInfo
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Information Matrices for 'lmeStruct' and 'glsStruct' Objects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-stats 
Requires:         R-CRAN-nlme 
Requires:         R-stats 

%description
Provides analytic derivatives and information matrices for fitted linear
mixed effects (lme) models and generalized least squares (gls) models
estimated using lme() (from package 'nlme') and gls() (from package
'nlme'), respectively. The package includes functions for estimating the
sampling variance-covariance of variance component parameters using the
inverse Fisher information. The variance components include the parameters
of the random effects structure (for lme models), the variance structure,
and the correlation structure. The expected and average forms of the
Fisher information matrix are used in the calculations, and models
estimated by full maximum likelihood or restricted maximum likelihood are
supported. The package also includes a function for estimating
standardized mean difference effect sizes (Pustejovsky, Hedges, and
Shadish (2014) <DOI:10.3102/1076998614547577>) based on fitted lme or gls
models.

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
