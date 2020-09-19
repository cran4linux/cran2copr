%global packname  hutilscpp
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Functions in C++

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-hutils 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-hutils 
Requires:         R-CRAN-magrittr 
Requires:         R-utils 

%description
Provides utility functions that are simply, frequently used, but may
require higher performance that what can be obtained from base R.
Incidentally provides support for 'reverse geocoding', such as matching a
point with its nearest neighbour in another array. Used as a complement to
package 'hutils' by sacrificing compilation or installation time for
higher running speeds. The name is a portmanteau of the author and 'Rcpp'.

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
