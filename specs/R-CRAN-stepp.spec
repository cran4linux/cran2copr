%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stepp
%global packver   3.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Subpopulation Treatment Effect Pattern Plot (STEPP)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
Requires:         R-methods 
Requires:         R-CRAN-car 
Requires:         R-CRAN-survival 
Requires:         R-splines 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 

%description
A method to explore the treatment-covariate interactions in survival or
generalized linear model (GLM) for continuous, binomial and count data
arising from two or more treatment arms of a clinical trial. A permutation
distribution approach to inference is implemented, based on permuting the
covariate values within each treatment group.

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
