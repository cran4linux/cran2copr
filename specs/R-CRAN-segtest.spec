%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  segtest
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for Segregation Distortion in Polyploids

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-minqa 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-updog 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-minqa 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-updog 

%description
Provides tests for segregation distortion in F1 polyploid populations
under different assumptions of meiosis. These tests can account for double
reduction, partial preferential pairing, and genotype uncertainty through
the use of genotype likelihoods. Parallelization support is provided.
Details of these methods are described in Gerard et al. (2025a)
<doi:10.1007/s00122-025-04816-z> and Gerard et al. (2025b)
<doi:10.1101/2025.06.23.661114>. Part of this material is based upon work
supported by the National Science Foundation under Grant No. 2132247.  The
opinions, findings, and conclusions or recommendations expressed are those
of the author and do not necessarily reflect the views of the National
Science Foundation.

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
