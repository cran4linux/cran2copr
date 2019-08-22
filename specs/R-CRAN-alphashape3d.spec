%global packname  alphashape3d
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Implementation of the 3D Alpha-Shape for the Reconstruction of3D Sets from a Point Cloud

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-rgl 

%description
Implementation in R of the alpha-shape of a finite set of points in the
three-dimensional space. The alpha-shape generalizes the convex hull and
allows to recover the shape of non-convex and even non-connected sets in
3D, given a random sample of points taken into it. Besides the computation
of the alpha-shape, this package provides users with functions to compute
the volume of the alpha-shape, identify the connected components and
facilitate the three-dimensional graphical visualization of the estimated
set.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
