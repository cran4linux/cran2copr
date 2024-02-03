%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PCGII
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Correlation Graph with Information Incorporation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-corpcor >= 1.6.10
BuildRequires:    R-CRAN-igraph >= 1.5.0.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-corpcor >= 1.6.10
Requires:         R-CRAN-igraph >= 1.5.0.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-Matrix 

%description
Large-scale gene expression studies allow gene network construction to
uncover associations among genes. This package is developed for estimating
and testing partial correlation graphs with prior information
incorporated.

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
