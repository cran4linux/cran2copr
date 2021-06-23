%global __brp_check_rpaths %{nil}
%global packname  FuncNN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-flux 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-flux 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-Matrix 

%description
A collection of functions which fit functional neural network models. In
other words, this package will allow users to build deep learning models
that have either functional or scalar responses paired with functional and
scalar covariates. We implement the theoretical discussion found in Thind,
Multani and Cao (2020) <arXiv:2006.09590> through the help of a main
fitting and prediction function as well as a number of helper functions to
assist with cross-validation, tuning, and the display of estimated
functional weights.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
