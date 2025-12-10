%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MIAmaxent
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Modular, Integrated Approach to Maximum Entropy Distribution Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-e1071 >= 1.6.7
BuildRequires:    R-CRAN-dplyr >= 0.4.3
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-e1071 >= 1.6.7
Requires:         R-CRAN-dplyr >= 0.4.3
Requires:         R-graphics 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for training, selecting, and evaluating maximum entropy (and
standard logistic regression) distribution models. This package provides
tools for user-controlled transformation of explanatory variables,
selection of variables by nested model comparison, and flexible model
evaluation and projection. It follows principles based on the maximum-
likelihood interpretation of maximum entropy modeling, and uses
infinitely- weighted logistic regression for model fitting. The package is
described in Vollering et al. (2019; <doi:10.1002/ece3.5654>).

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
