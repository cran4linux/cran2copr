%global __brp_check_rpaths %{nil}
%global packname  SMLE
%global packver   2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Feature Screening via Sparse MLE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvnfast 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvnfast 

%description
Feature screening is a powerful tool in processing ultrahigh dimensional
data. It attempts to screen out most irrelevant features in preparation
for a more elaborate analysis. Xu and Chen
(2014)<doi:10.1080/01621459.2013.879531> proposed an effective screening
method SMLE, which naturally incorporates the joint effects among features
in the screening process. This package provides an efficient
implementation of SMLE-screening for high-dimensional linear, logistic,
and Poisson models. The package also provides a function for conducting
accurate post-screening feature selection based on an iterative
hard-thresholding procedure and a user-specified selection criterion.

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
