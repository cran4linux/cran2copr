%global packname  gensphere
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Generalized Spherical Distributions

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvmesh 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-SphericalCubature 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-SimplicialCubature 
Requires:         R-CRAN-mvmesh 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-SphericalCubature 
Requires:         R-CRAN-rgl 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-SimplicialCubature 

%description
Define and compute with generalized spherical distributions - multivariate
probability laws that are specified by a star shaped contour (directional
behavior) and a radial component.

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
