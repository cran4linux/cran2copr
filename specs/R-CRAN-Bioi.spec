%global packname  Bioi
%global packver   0.2.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.10
Release:          1%{?dist}%{?buildtag}
Summary:          Biological Image Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-dplyr >= 0.7.4
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-dplyr >= 0.7.4
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-CRAN-igraph 

%description
Single linkage clustering and connected component analyses are often
performed on biological images. 'Bioi' provides a set of functions for
performing these tasks. This functionality is implemented in several key
functions that can extend to from 1 to many dimensions. The single linkage
clustering method implemented here can be used on n-dimensional data sets,
while connected component analyses are limited to 3 or fewer dimensions.

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
