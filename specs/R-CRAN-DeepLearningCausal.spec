%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DeepLearningCausal
%global packver   0.0.107
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.107
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference with Super Learner and Deep Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-keras3 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-keras3 
Requires:         R-CRAN-Hmisc 

%description
Functions for deep learning estimation of Conditional Average Treatment
Effects (CATEs) from meta-learner models and Population Average Treatment
Effects on the Treated (PATT) in settings with treatment noncompliance
using reticulate, TensorFlow and Keras3. Functions in the package also
implements the conformal prediction framework that enables computation and
illustration of conformal prediction (CP) intervals for estimated
individual treatment effects (ITEs) from meta-learner models. Additional
functions in the package permit users to estimate the meta-learner CATEs
and the PATT in settings with treatment noncompliance using weighted
ensemble learning via the super learner approach and R neural networks.

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
