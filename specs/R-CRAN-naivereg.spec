%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  naivereg
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Additive Instrumental Variable Estimator and Related IV Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ncvreg 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 
Requires:         R-splines 
Requires:         R-CRAN-gmm 
Requires:         R-stats 
Requires:         R-CRAN-ncvreg 
Requires:         R-CRAN-glmnet 

%description
In empirical studies, instrumental variable (IV) regression is the
signature method to solve the endogeneity problem. If we enforce the
exogeneity condition of the IV, it is likely that we end up with a large
set of IVs without knowing which ones are good. Also, one could face the
model uncertainty for structural equation, as large micro dataset is
commonly available nowadays. This package uses adaptive group lasso and
B-spline methods to select the nonparametric components of the IV
function, with the linear function being a special case (naivereg). The
package also incorporates two stage least squares estimator (2SLS),
generalized method of moment (GMM), generalized empirical likelihood (GEL)
methods post instrument selection, logistic-regression instrumental
variables estimator (LIVE, for dummy endogenous variable problem),
double-selection plus instrumental variable estimator (DS-IV) and double
selection plus logistic regression instrumental variable estimator
(DS-LIVE), where the double selection methods are useful for
high-dimensional structural equation models. The naivereg is nonparametric
version of 'ivregress' in 'Stata' with IV selection and high dimensional
features. The package is based on the paper by Q. Fan and W. Zhong,
"Nonparametric Additive Instrumental Variable Estimator: A Group Shrinkage
Estimation Perspective" (2018), Journal of Business & Economic Statistics
<doi:10.1080/07350015.2016.1180991> as well as a series of working papers
led by the same authors.

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
