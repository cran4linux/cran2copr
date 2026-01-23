%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MATES
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-View Aggregated Two Sample Tests

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magrittr 

%description
Implements the Multi-view Aggregated Two-Sample (MATES) test, a powerful
nonparametric method for testing equality of two multivariate
distributions. The method constructs multiple graph-based statistics from
various perspectives (views) including different distance metrics, graph
types (nearest neighbor graphs, minimum spanning trees, and robust nearest
neighbor graphs), and weighting schemes. These statistics are then
aggregated through a quadratic form to achieve improved statistical power.
The package provides both asymptotic closed-form inference and
permutation-based testing procedures. For methodological details, see Cai
and others (2026+) <doi:10.48550/arXiv.2412.16684>.

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
