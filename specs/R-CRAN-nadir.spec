%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nadir
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Super Learning with Flexible Formulas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-earth 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-hal9001 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-origami 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-xgboost 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-earth 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-hal9001 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-origami 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-xgboost 

%description
A functional programming based implementation of the super learner
algorithm with an emphasis on supporting the use of formulas to specify
learners. This approach offers several improvements compared to past
implementations including the ability to easily use random-effects
specified in formulas (like y ~ (age | strata) + ...) and construction of
new learners is as simple as writing and passing a new function. The super
learner algorithm was originally described in van der Laan et al. (2007)
<https://biostats.bepress.com/ucbbiostat/paper222/>.

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
