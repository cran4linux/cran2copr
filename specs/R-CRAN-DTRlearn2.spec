%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DTRlearn2
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Learning Methods for Optimizing Dynamic Treatment Regimes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-WeightSVM 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-WeightSVM 

%description
We provide a comprehensive software to estimate general K-stage DTRs from
SMARTs with Q-learning and a variety of outcome-weighted learning methods.
Penalizations are allowed for variable selection and model regularization.
With the outcome-weighted learning scheme, different loss functions - SVM
hinge loss, SVM ramp loss, binomial deviance loss, and L2 loss - are
adopted to solve the weighted classification problem at each stage;
augmentation in the outcomes is allowed to improve efficiency. The
estimated DTR can be easily applied to a new sample for individualized
treatment recommendations or DTR evaluation.

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
