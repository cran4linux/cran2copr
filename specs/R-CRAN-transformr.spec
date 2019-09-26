%global packname  transformr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Polygon and Path Transformations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-tweenr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-CRAN-tweenr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-lpSolve 

%description
In order to smoothly animate the transformation of polygons and paths,
many aspects needs to be taken into account, such as differing number of
control points, changing center of rotation, etc. The 'transformr' package
provides an extensive framework for manipulating the shapes of polygons
and paths and can be seen as the spatial brother to the 'tweenr' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
