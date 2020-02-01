%global packname  deldir
%global packver   0.1-23
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.23
Release:          1%{?dist}
Summary:          Delaunay Triangulation and Dirichlet (Voronoi) Tessellation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 0.99
Requires:         R-core >= 0.99
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.
Plots triangulations and tessellations in various ways.  Clips
tessellations to sub-windows. Calculates perimeters of tessellations.
Summarises information about the tiles of the tessellation.

%prep
%setup -q -c -n %{packname}


%build

%install
test $(gcc -dumpversion) -ge 10 && export PKG_FFLAGS=-fallow-argument-mismatch
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/code.discarded
%doc %{rlibdir}/%{packname}/err.list
%doc %{rlibdir}/%{packname}/ex.out
%doc %{rlibdir}/%{packname}/ratfor
%doc %{rlibdir}/%{packname}/READ_ME
%doc %{rlibdir}/%{packname}/SavedRatfor
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
