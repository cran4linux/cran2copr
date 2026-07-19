%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lightgbm
%global packver   4.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Light Gradient Boosting Machine

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-R6 >= 2.4.0
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Matrix >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 >= 2.4.0
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Matrix >= 1.1.0
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-utils 

%description
Tree based algorithms can be improved by introducing boosting frameworks.
'LightGBM' is one such framework, based on Ke, Guolin et al. (2017)
<https://proceedings.neurips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html>.
This package offers an R interface to work with it. It is designed to be
distributed and efficient with the following advantages: 1. Faster
training speed and higher efficiency. 2. Lower memory usage. 3. Better
accuracy. 4. Parallel learning supported. 5. Capable of handling
large-scale data. In recognition of these advantages, 'LightGBM' has been
widely-used in many winning solutions of machine learning competitions.
Comparison experiments on public datasets suggest that 'LightGBM' can
outperform existing boosting frameworks on both efficiency and accuracy,
with significantly lower memory consumption. In addition, parallel
experiments suggest that in certain circumstances, 'LightGBM' can achieve
a linear speed-up in training time by using multiple machines.

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
