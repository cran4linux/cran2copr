%global packname  FSinR
%global packver   2.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-prodlim 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-class 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-mlbench 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-prodlim 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-e1071 

%description
Feature subset selection algorithms modularized in search algorithms and
measure utilities. Full list and more information available at
<https://dicits.ugr.es/software/FSinR/>.

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
