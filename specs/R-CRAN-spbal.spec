%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spbal
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Spatially Balanced Sampling Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-units 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppThread 
Requires:         R-CRAN-units 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 

%description
Encapsulates a number of spatially balanced sampling algorithms, namely,
Balanced Acceptance Sampling (equal, unequal, seed point, panels), Halton
frames (for discretizing a continuous resource), Halton Iterative
Partitioning (equal probability) and Simple Random Sampling. Robertson, B.
L., Brown, J. A., McDonald, T. and Jaksons, P. (2013)
<doi:10.1111/biom.12059>. Robertson, B. L., McDonald, T., Price, C. J. and
Brown, J. A. (2017) <doi:10.1016/j.spl.2017.05.004>. Robertson, B. L.,
McDonald, T., Price, C. J. and Brown, J. A. (2018)
<doi:10.1007/s10651-018-0406-6>. Robertson, B. L., van Dam-Bates, P. and
Gansell, O. (2021a) <doi:10.1007/s10651-020-00481-1>. Robertson, B. L.,
Davies, P., Gansell, O., van Dam-Bates, P., McDonald, T. (2025)
<doi:10.1111/anzs.12435>.

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
