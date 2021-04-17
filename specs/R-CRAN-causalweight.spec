%global packname  causalweight
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation Methods for Causal Inference Based on Inverse Probability Weighting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-LARF 
BuildRequires:    R-CRAN-hdm 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-fastDummies 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-np 
Requires:         R-CRAN-LARF 
Requires:         R-CRAN-hdm 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-fastDummies 

%description
Various estimators of causal effects based on inverse probability
weighting, doubly robust estimation, and double machine learning.
Specifically, the package includes methods for estimating average
treatment effects, direct and indirect effects in causal mediation
analysis, and dynamic treatment effects. The models refer to studies of
Froelich (2007) <doi:10.1016/j.jeconom.2006.06.004>, Huber (2012)
<doi:10.3102/1076998611411917>, Huber (2014)
<doi:10.1080/07474938.2013.806197>, Huber (2014) <doi:10.1002/jae.2341>,
Froelich and Huber (2017) <doi:10.1111/rssb.12232>, Hsu, Huber, Lee, and
Lettry (2020) <doi:10.1002/jae.2765>, and others.

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
