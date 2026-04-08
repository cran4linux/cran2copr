%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tf
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          S3 Classes and Methods for Tidy Functional Data

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr >= 1.0.0
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-purrr >= 1.0.0
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-methods 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
Provides S3 vector types for functional data represented on grids, in
spline bases, or via functional principal components. Supports arithmetic
and summary methods, plotting, derivation, integration, smoothing,
registration, and data import/export for these functional vectors.
Includes data-wrangling tools for re-evaluation, subsetting,
sub-assignment, zooming into sub-domains, and extracting functional
features such as minima, maxima, and their locations. Enables joint
analysis of functional and scalar variables by integrating functional
vectors into standard data frames.

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
