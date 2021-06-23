%global __brp_check_rpaths %{nil}
%global packname  biokNN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bi-Objective k-Nearest Neighbors Imputation for Multilevel Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-mice 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-desc 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-mitml 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-mice 
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-desc 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-mitml 

%description
The bi-objective k-nearest neighbors method (biokNN) is an imputation
method designed to estimate missing values on data with a multilevel
structure. The original algorithm is an extension of the k-nearest
neighbors method proposed by Bertsimas et al. (2017)
(<https://jmlr.org/papers/v18/17-073.html>) using a bi-objective approach.
A brief description of the method can be found in Cubillos (2021)
(<https://pure.au.dk/portal/files/214627979/biokNN.pdf>). The 'biokNN'
package provides an R implementation of the method for datasets with
continuous variables (e.g. employee productivity, student grades) and a
categorical class variable (e.g. department, school). Given an incomplete
dataset with such structure, this package produces complete datasets using
both single and multiple imputation, including visualization tools to
better understand the pattern of the missing values.

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
