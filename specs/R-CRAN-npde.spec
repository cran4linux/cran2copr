%global __brp_check_rpaths %{nil}
%global packname  npde
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Normalised Prediction Distribution Errors for Nonlinear Mixed-Effect Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mclust 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-rlang 

%description
Provides routines to compute normalised prediction distribution errors, a
metric designed to evaluate non-linear mixed effect models such as those
used in pharmacokinetics and pharmacodynamics.

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
