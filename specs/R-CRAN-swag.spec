%global packname  swag
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Wrapper Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-caret 
Requires:         R-stats 

%description
An algorithm that trains a meta-learning procedure that combines screening
and wrapper methods to find a set of extremely low-dimensional attribute
combinations. This package works on top of the 'caret' package and
proceeds in a forward-step manner. More specifically, it builds and tests
learners starting from very few attributes until it includes a maximal
number of attributes by increasing the number of attributes at each step.
Hence, for each fixed number of attributes, the algorithm tests various
(randomly selected) learners and picks those with the best performance in
terms of training error. Throughout, the algorithm uses the information
coming from the best learners at the previous step to build and test
learners in the following step. In the end, it outputs a set of strong
low-dimensional learners.

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
