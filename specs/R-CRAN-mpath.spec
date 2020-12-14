%global packname  mpath
%global packver   0.4-2.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2.17
Release:          1%{?dist}%{?buildtag}
Summary:          Regularized Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-pamr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pscl 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-bst 
BuildRequires:    R-CRAN-WeightSVM 
Requires:         R-methods 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-pamr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pscl 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-bst 
Requires:         R-CRAN-WeightSVM 

%description
Algorithms compute concave convex (CC) estimators including robust
(penalized) generalized linear models and robust support vector machines
via the COCO - composite optimization by conjugation operator. The package
also contains penalized Poisson, negative binomial, zero-inflated Poisson,
zero-inflated negative binomial regression models and robust models with
non-convex loss functions. See Wang et al. (2014) <doi:10.1002/sim.6314>,
Wang et al. (2015) <doi:10.1002/bimj.201400143>, Wang et al. (2016)
<doi:10.1177/0962280214530608>, Wang (2019) <arXiv:1912.11119>, Wang
(2020) <arXiv:2010.02848>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
