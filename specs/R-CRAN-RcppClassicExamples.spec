%global packname  RcppClassicExamples
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Examples using 'RcppClassic' to Interface R and C++

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildRequires:    R-CRAN-RcppClassic >= 0.9.3
BuildRequires:    R-CRAN-Rcpp >= 0.10.2
Requires:         R-CRAN-RcppClassic >= 0.9.3
Requires:         R-CRAN-Rcpp >= 0.10.2

%description
The 'Rcpp' package contains a C++ library that facilitates the integration
of R and C++ in various ways via a rich API. This API was preceded by an
earlier version which has been deprecated since 2010 (but is still
supported to provide backwards compatibility in the package
'RcppClassic').  This package 'RcppClassicExamples' provides usage
examples for the older, deprecated API. There is also a corresponding
package 'RcppExamples' with examples for the newer, current API which we
strongly recommend as the basis for all new development.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
