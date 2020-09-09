%global packname  nabor
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Wraps 'libnabo', a Fast K Nearest Neighbour Library for Low Dimensions

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-BH >= 1.54.0.4
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.11.2
Requires:         R-methods 

%description
An R wrapper for 'libnabo', an exact or approximate k nearest neighbour
library which is optimised for low dimensional spaces (e.g. 3D). 'libnabo'
has speed and space advantages over the 'ANN' library wrapped by package
'RANN'. 'nabor' includes a knn function that is designed as a drop-in
replacement for 'RANN' function nn2. In addition, objects which include
the k-d tree search structure can be returned to speed up repeated queries
of the same set of target points.

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
