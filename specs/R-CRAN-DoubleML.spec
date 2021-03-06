%global packname  DoubleML
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Double Machine Learning in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.4.1
BuildRequires:    R-CRAN-data.table >= 1.12.8
BuildRequires:    R-CRAN-mlr3 >= 0.5.0
BuildRequires:    R-CRAN-mlr3tuning >= 0.3.0
BuildRequires:    R-CRAN-mlr3learners >= 0.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-clusterGeneration 
BuildRequires:    R-CRAN-readstata13 
Requires:         R-CRAN-R6 >= 2.4.1
Requires:         R-CRAN-data.table >= 1.12.8
Requires:         R-CRAN-mlr3 >= 0.5.0
Requires:         R-CRAN-mlr3tuning >= 0.3.0
Requires:         R-CRAN-mlr3learners >= 0.3.0
Requires:         R-stats 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-mvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-clusterGeneration 
Requires:         R-CRAN-readstata13 

%description
Implementation of the double/debiased machine learning framework of
Chernozhukov et al. (2018) <doi:10.1111/ectj.12097> for partially linear
regression models, partially linear instrumental variable regression
models, interactive regression models and interactive instrumental
variable regression models. 'DoubleML' allows estimation of the nuisance
parts in these models by machine learning methods and computation of the
Neyman orthogonal score functions. 'DoubleML' is built on top of 'mlr3'
and the 'mlr3' ecosystem. The object-oriented implementation of 'DoubleML'
based on the 'R6' package is very flexible.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
