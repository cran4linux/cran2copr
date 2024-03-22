%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  melt
%global packver   1.11.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multiple Empirical Likelihood Tests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-BH 
BuildRequires:    R-CRAN-dqrng 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-checkmate 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Performs multiple empirical likelihood tests. It offers an easy-to-use
interface and flexibility in specifying hypotheses and calibration
methods, extending the framework to simultaneous inferences.  The core
computational routines are implemented using the 'Eigen' 'C++' library and
'RcppEigen' interface, with 'OpenMP' for parallel computation.  Details of
the testing procedures are provided in Kim, MacEachern, and Peruggia
(2023) <doi:10.1080/10485252.2023.2206919>. A companion paper by Kim,
MacEachern, and Peruggia (2024) <doi:10.18637/jss.v108.i05> is available
for further information. This work was supported by the U.S. National
Science Foundation under Grants No. SES-1921523 and DMS-2015552.

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
