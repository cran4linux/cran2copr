%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ATE.ERROR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating ATE with Misclassified Outcomes and Mismeasured Covariates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rlang 
Requires:         R-stats 

%description
Addressing measurement error in covariates and misclassification in binary
outcome variables within causal inference, the 'ATE.ERROR' package
implements inverse probability weighted estimation methods proposed by Shu
and Yi (2017, <doi:10.1177/0962280217743777>; 2019,
<doi:10.1002/sim.8073>). These methods correct errors to accurately
estimate average treatment effects (ATE). The package includes two main
functions: ATE.ERROR.Y() for handling misclassification in the outcome
variable and ATE.ERROR.XY() for correcting both outcome misclassification
and covariate measurement error. It employs logistic regression for
treatment assignment and uses bootstrap sampling to calculate standard
errors and confidence intervals, with simulated datasets provided for
practical demonstration.

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
