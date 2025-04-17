%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flexFitR
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Non-Linear Least Square Model Fitting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-agriutilities 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-agriutilities 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Provides tools for flexible non-linear least squares model fitting using
general-purpose optimization techniques. The package supports a variety of
optimization algorithms, including those provided by the 'optimx' package,
making it suitable for handling complex non-linear models. Features
include parallel processing support via the 'future' and 'foreach'
packages, comprehensive model diagnostics, and visualization capabilities.
Implements methods described in Nash and Varadhan (2011,
<doi:10.18637/jss.v043.i09>).

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
