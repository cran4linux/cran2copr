%global __brp_check_rpaths %{nil}
%global packname  biganalytics
%global packver   1.1.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.21
Release:          3%{?dist}%{?buildtag}
Summary:          Utilities for 'big.matrix' Objects from Package 'bigmemory'

License:          LGPL-3 | Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-bigmemory >= 4.0.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-biglm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-bigmemory >= 4.0.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-biglm 

%description
Extend the 'bigmemory' package with various analytics. Functions
'bigkmeans' and 'binit' may also be used with native R objects. For
'tapply'-like functions, the bigtabulate package may also be helpful. For
linear algebra support, see 'bigalgebra'.  For mutex (locking) support for
advanced shared-memory usage, see 'synchronicity'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
