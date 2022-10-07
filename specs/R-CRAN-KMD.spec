%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  KMD
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Measure of Multi-Sample Dissimilarity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-mlpack 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-igraph 

%description
Implementations of the kernel measure of multi-sample dissimilarity (KMD)
between several samples using K-nearest neighbor graphs and minimum
spanning trees. The KMD measures the dissimilarity between multiple
samples, based on the observations from them. It converges to the
population quantity (depending on the kernel) which is between 0 and 1. A
small value indicates the multiple samples are from the same distribution,
and a large value indicates the corresponding distributions are different.
The population quantity is 0 if and only if all distributions are the
same, and 1 if and only if all distributions are mutually singular. The
package also implements the tests based on KMD for H0: the M distributions
are equal against H1: not all the distributions are equal. Both
permutation test and asymptotic test are available. These tests are
consistent against all alternatives where at least two samples have
different distributions. For more details on KMD and the associated tests,
see Huang, Z. and B. Sen (2022) <arXiv:2210.00634>.

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
