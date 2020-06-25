%global packname  lazyarray
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Persistent Large Data Array with Lazy-Loading on Demand

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-fstcore 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-CRAN-R6 
Requires:         R-CRAN-fstcore 
Requires:         R-CRAN-yaml 

%description
Multi-threaded serialization of compressed array that fully utilizes
modern solid state drives. It allows to store and load extremely large
data on demand within seconds without occupying too much memories. With
data stored on hard drive, a lazy-array data can be loaded, shared across
multiple R sessions. For arrays with partition mode on, multiple R
sessions can write to a same array simultaneously along the last dimension
(partition).

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

%files
%{rlibdir}/%{packname}
