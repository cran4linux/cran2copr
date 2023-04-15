%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  embed
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extra Recipes for Encoding Predictors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-recipes >= 1.0.4
BuildRequires:    R-CRAN-rlang >= 0.4.10
BuildRequires:    R-CRAN-generics >= 0.1.0
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tensorflow 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-recipes >= 1.0.4
Requires:         R-CRAN-rlang >= 0.4.10
Requires:         R-CRAN-generics >= 0.1.0
Requires:         R-CRAN-glue 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-tensorflow 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-withr 

%description
Predictors can be converted to one or more numeric representations using a
variety of methods. Effect encodings using simple generalized linear
models <arXiv:1611.09477> or nonlinear models <arXiv:1604.06737> can be
used.  There are also functions for dimension reduction and other
approaches.

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
