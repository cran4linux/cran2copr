%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  seqimpute
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Imputation of Missing Data in Sequence Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Amelia 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-TraMineR 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-swfscMisc 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dfidx 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-mlr 
BuildRequires:    R-CRAN-nnet 
Requires:         R-CRAN-Amelia 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-TraMineR 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-swfscMisc 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dfidx 
Requires:         R-CRAN-mice 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-mlr 
Requires:         R-CRAN-nnet 

%description
Multiple imputation of missing data present in a dataset through the
prediction based on either a random forest or a multinomial regression
model. Covariates and time-dependant covariates can be included in the
model. The prediction of the missing values is based on the method of
Halpin (2012)
<https://researchrepository.ul.ie/articles/report/Multiple_imputation_for_life-course_sequence_data/19839736>.

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
