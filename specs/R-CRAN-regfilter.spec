%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  regfilter
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Elimination of Noisy Samples in Regression Datasets using Noise Filters

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-UBL 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-entropy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-UBL 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-entropy 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sf 

%description
Traditional noise filtering methods aim at removing noisy samples from a
classification dataset. This package adapts classic and recent filtering
techniques for use in regression problems, and it also incorporates
methods specifically designed for regression data. In order to do this, it
uses approaches proposed in the specialized literature, such as Martin et
al. (2021) [<doi:10.1109/ACCESS.2021.3123151>] and Arnaiz-Gonzalez et al.
(2016) [<doi:10.1016/j.eswa.2015.12.046>]. Thus, the goal of the
implemented noise filters is to eliminate samples with noise in regression
datasets.

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
