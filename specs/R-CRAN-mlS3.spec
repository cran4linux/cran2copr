%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlS3
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Unified S3 Interface to Machine Learning Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lightgbm 
BuildRequires:    R-CRAN-ranger 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lightgbm 
Requires:         R-CRAN-ranger 

%description
Provides a unified and consistent S3 interface for training and predicting
with a variety of machine learning models in R. The package wraps popular
algorithms (e.g., from 'glmnet', 'lightgbm', 'ranger', 'e1071', and
'caret') under a common workflow based on simple wrap_*() and predict()
functions, allowing users to switch between models without changing their
code structure. It supports both classification and regression tasks and
facilitates rapid experimentation, benchmarking, and comparison of models.
By abstracting away package-specific APIs while preserving flexibility in
parameter specification, the package streamlines machine learning
workflows and promotes reproducibility.

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
