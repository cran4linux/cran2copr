%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Ricrt
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Randomization Inference of Clustered Randomized Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-tidyverse 
Requires:         R-stats 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 

%description
Methods for randomization inference in group-randomized trials.
Specifically, it can be used to analyze the treatment effect of stratified
data with multiple clusters in each stratum with treatment given on
cluster level. User may also input as many covariates as they want to fit
the data. Methods are described by Dylan S Small et al., (2012)
<doi:10.1198/016214507000000897>.

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
