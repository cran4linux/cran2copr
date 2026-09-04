%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3automl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Machine Learning for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbotk >= 1.7.1
BuildRequires:    R-CRAN-mlr3 >= 1.6.0
BuildRequires:    R-CRAN-mlr3tuning >= 1.6.0
BuildRequires:    R-CRAN-rush >= 1.2.1
BuildRequires:    R-CRAN-mlr3mbo >= 1.2.0
BuildRequires:    R-CRAN-paradox >= 1.0.1
BuildRequires:    R-CRAN-mlr3misc >= 0.15.1
BuildRequires:    R-CRAN-mlr3learners >= 0.14.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
Requires:         R-CRAN-bbotk >= 1.7.1
Requires:         R-CRAN-mlr3 >= 1.6.0
Requires:         R-CRAN-mlr3tuning >= 1.6.0
Requires:         R-CRAN-rush >= 1.2.1
Requires:         R-CRAN-mlr3mbo >= 1.2.0
Requires:         R-CRAN-paradox >= 1.0.1
Requires:         R-CRAN-mlr3misc >= 0.15.1
Requires:         R-CRAN-mlr3learners >= 0.14.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lhs 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-R6 
Requires:         R-utils 

%description
Flexible automated machine learning (AutoML) system for the 'mlr3'
ecosystem. Automatically selects a suitable machine learning algorithm and
tunes its hyperparameters for a given task. Constructs preprocessing
pipelines with multiple parallel branches using 'mlr3pipelines' and
jointly optimizes them together with the learners using 'mlr3tuning'. The
optimization is driven by asynchronous decentralized Bayesian optimization
by Egele et al. (2023) <doi:10.1109/e-Science58273.2023.10254839>.

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
