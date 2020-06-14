%global packname  SphericalCubature
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          2%{?dist}
Summary:          Numerical Integration over Spheres and Balls in n-Dimensions;Multivariate Polar Coordinates

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-SimplicialCubature 
BuildRequires:    R-CRAN-mvmesh 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-SimplicialCubature 
Requires:         R-CRAN-mvmesh 
Requires:         R-CRAN-abind 

%description
Provides several methods to integrate functions over the unit sphere and
ball in n-dimensional Euclidean space.  Routines for converting to/from
multivariate polar/spherical coordinates are also provided.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
