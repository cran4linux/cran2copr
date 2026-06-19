%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  varGuid
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Variance-Guided Regression Improving Upon OLS and ANOVA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-sandwich 

%description
Fits variance-guided linear regression models that provide an alternative
to ordinary least squares (OLS) for general linear-model design matrices,
including ANOVA-style encodings. The methods use an iteratively reweighted
least squares estimator or an iteratively reweighted lasso estimator and
implement the global linear mean-variance model from the associated 2026
Statistics in Medicine article <doi:10.1002/sim.70632>. Under the
assumptions in that paper, the estimator matches the homoscedastic
baseline in population predictive quasi-risk when variance is constant and
improves on it when the variance depends on covariates. The grouping-based
nonlinear prediction extension from Section 3 is available in the
development version on GitHub.

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
