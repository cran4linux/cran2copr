%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RcppCNPy
%global packver   0.2.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.13
Release:          1%{?dist}%{?buildtag}
Summary:          Read-Write Support for 'NumPy' Files via 'Rcpp'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 

%description
The 'cnpy' library written by Carl Rogers provides read and write
facilities for files created with (or for) the 'NumPy' extension for
'Python'. Vectors and matrices of numeric types can be read or written to
and from files as well as compressed files. Support for integer files is
available if the package has been built with as C++11 which should be the
default on all platforms since the release of R 3.3.0.

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
