%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MEGB
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Gradient Boosting for Longitudinal Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-latex2exp 
Requires:         R-stats 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-latex2exp 

%description
Gradient boosting is a powerful statistical learning method known for its
ability to model complex relationships between predictors and outcomes
while performing inherent variable selection. However, traditional
gradient boosting methods lack flexibility in handling longitudinal data
where within-subject correlations play a critical role. In this package,
we propose a novel approach Mixed Effect Gradient Boosting ('MEGB'),
designed specifically for high-dimensional longitudinal data. 'MEGB'
incorporates a flexible semi-parametric model that embeds random effects
within the gradient boosting framework, allowing it to account for
within-individual covariance over time. Additionally, the method
efficiently handles scenarios where the number of predictors greatly
exceeds the number of observations (p>>n) making it particularly suitable
for genomics data and other large-scale biomedical studies.

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
