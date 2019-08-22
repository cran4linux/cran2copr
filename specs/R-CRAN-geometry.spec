%global packname  geometry
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Mesh Generation and Surface Tessellation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-linprog 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-linprog 

%description
Makes the 'Qhull' library <http://www.qhull.org> available in R, in a
similar manner as in Octave and MATLAB. Qhull computes convex hulls,
Delaunay triangulations, halfspace intersections about a point, Voronoi
diagrams, furthest-site Delaunay triangulations, and furthest-site Voronoi
diagrams. It runs in 2D, 3D, 4D, and higher dimensions. It implements the
Quickhull algorithm for computing the convex hull. Qhull does not support
constrained Delaunay triangulations, or mesh generation of non-convex
objects, but the package does include some R functions that allow for
this.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
