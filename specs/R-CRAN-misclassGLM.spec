%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  misclassGLM
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Computation of Generalized Linear Models with Misclassified Covariates Using Side Information

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-mlogit 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-mlogit 

%description
Estimates models that extend the standard GLM to take misclassification
into account. The models require side information from a secondary data
set on the misclassification process, i.e. some sort of misclassification
probabilities conditional on some common covariates. A detailed
description of the algorithm can be found in Dlugosz, Mammen and Wilke
(2015) <https://ftp.zew.de/pub/zew-docs/dp/dp15043.pdf>.

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
