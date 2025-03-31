%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dtComb
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Combination of Diagnostic Tests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC >= 1.18.0
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-epiR 
BuildRequires:    R-CRAN-gam 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-OptimalCutpoints 
Requires:         R-CRAN-pROC >= 1.18.0
Requires:         R-CRAN-caret 
Requires:         R-CRAN-epiR 
Requires:         R-CRAN-gam 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-OptimalCutpoints 

%description
A system for combining two diagnostic tests using various approaches that
include statistical and machine-learning-based methodologies. These
approaches are divided into four groups: linear combination methods,
non-linear combination methods, mathematical operators, and machine
learning algorithms. See the <https://biotools.erciyes.edu.tr/dtComb/>
website for more information, documentation, and examples.

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
