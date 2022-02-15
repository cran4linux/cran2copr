%global __brp_check_rpaths %{nil}
%global packname  gofcat
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Goodness-of-Fit Measures for Categorical Response Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-VGAM >= 1.1.4
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-VGAM >= 1.1.4
Requires:         R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-stringr 

%description
A post-estimation method for categorical response models (CRM). Inputs
from objects of class serp(), clm(), polr(), multinom(), mlogit(), vglm()
and glm() are currently supported. Available tests include the
Hosmer-Lemeshow tests for the binary, multinomial and ordinal logistic
regression; the Lipsitz and the Pulkstenis-Robinson tests for the ordinal
models. The proportional odds, adjacent-category, and constrained
continuation-ratio models are particularly supported at ordinal level.
Tests for the proportional odds assumptions in ordinal models are also
possible with the Brant and the Likelihood-Ratio tests. Moreover, several
summary measures of predictive strength (Pseudo R-squared), and some
useful error metrics, including, the brier score, misclassification rate
and logloss are also available for the binary, multinomial and ordinal
models. Ugba, E. R. and Gertheiss, J. (2018)
<http://www.statmod.org/workshops_archive_proceedings_2018.html>.

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
