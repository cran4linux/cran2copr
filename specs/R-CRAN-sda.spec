%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sda
%global packver   1.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage Discriminant Analysis and CAT Score Variable Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.10
BuildRequires:    R-CRAN-entropy >= 1.3.2
BuildRequires:    R-CRAN-fdrtool >= 1.2.18
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-corpcor >= 1.6.10
Requires:         R-CRAN-entropy >= 1.3.2
Requires:         R-CRAN-fdrtool >= 1.2.18
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides an efficient framework for high-dimensional linear and diagonal
discriminant analysis with variable selection.  The classifier is trained
using James-Stein-type shrinkage estimators and predictor variables are
ranked using correlation-adjusted t-scores (CAT scores).  Variable
selection error is controlled using false non-discovery rates or higher
criticism.

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
