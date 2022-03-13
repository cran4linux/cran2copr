%global __brp_check_rpaths %{nil}
%global packname  TreeDimensionTest
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Trajectory Presence and Heterogeneity in Multivariate Data

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.2
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-nFactors 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp >= 1.0.2
Requires:         R-CRAN-mlpack 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-nFactors 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rdpack 

%description
Testing for trajectory presence and heterogeneity on multivariate data.
Two statistical methods (Tenha & Song 2022)
<doi:10.1371/journal.pcbi.1009829> are implemented. The tree dimension
test quantifies the statistical evidence for trajectory presence. The
subset specificity measure summarizes pattern heterogeneity using the
minimum subtree cover. There is no user tunable parameters for either
method. Examples are included to illustrate how to use the methods on
single-cell data for studying gene and pathway expression dynamics and
pathway expression specificity.

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
