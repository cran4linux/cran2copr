%global packname  bigsparser
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Sparse Matrix Format with Data on Disk

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-bigassertr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-bigassertr 
Requires:         R-methods 

%description
Provides a sparse matrix format with data stored on disk, to be used in
both R and C++. This is intended for more efficient use of sparse data in
C++ and also when parallelizing, since data on disk does not need copying.
Only a limited number of features will be implemented. For now, conversion
can be performed from a 'dgCMatrix' of R package 'Matrix'.

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
