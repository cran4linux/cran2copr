%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqimpute
%global packver   2.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation of Missing Data in Sequence Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-CRAN-TraMineRextras 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-parallelly 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-nnet 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-rms 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-TraMineR 
Requires:         R-CRAN-TraMineRextras 
Requires:         R-utils 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-parallelly 

%description
Multiple imputation of missing data in a dataset using MICT or MICT-timing
methods. The core idea of the algorithms is to fill gaps of missing data,
which is the typical form of missing data in a longitudinal setting,
recursively from their edges. Prediction is based on either a multinomial
or random forest regression model. Covariates and time-dependent
covariates can be included in the model.

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
