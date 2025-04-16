%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cds
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Constrained Dual Scaling for Detecting Response Styles

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-limSolve 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-limSolve 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-copula 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
This is an implementation of constrained dual scaling for detecting
response styles in categorical data, including utility functions. The
procedure involves adding additional columns to the data matrix
representing the boundaries between the rating categories. The resulting
matrix is then doubled and analyzed by dual scaling. One-dimensional
solutions are sought which provide optimal scores for the rating
categories. These optimal scores are constrained to follow monotone
quadratic splines. Clusters are introduced within which the response
styles can vary. The type of response style present in a cluster can be
diagnosed from the optimal scores for said cluster, and this can be used
to construct an imputed version of the data set which adjusts for response
styles.

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
