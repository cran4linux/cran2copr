%global packname  treeplyr
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          'dplyr' Functionality for Matched Tree and Data Objects

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-ape >= 3.0.6
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.10.3
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-geiger 
Requires:         R-CRAN-ape >= 3.0.6
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-Rcpp >= 0.10.3
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-geiger 

%description
Matches phylogenetic trees and trait data, and allows simultaneous
manipulation of the tree and data using 'dplyr'.

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
