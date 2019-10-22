%global packname  restlos
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Robust Estimation of Location and Scatter

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-limSolve >= 1.5.5.1
BuildRequires:    R-CRAN-igraph >= 1.0.1
BuildRequires:    R-CRAN-rgl >= 0.95.1247
BuildRequires:    R-CRAN-som >= 0.3.5
BuildRequires:    R-CRAN-geometry >= 0.3.5
Requires:         R-CRAN-limSolve >= 1.5.5.1
Requires:         R-CRAN-igraph >= 1.0.1
Requires:         R-CRAN-rgl >= 0.95.1247
Requires:         R-CRAN-som >= 0.3.5
Requires:         R-CRAN-geometry >= 0.3.5

%description
The restlos package provides algorithms for robust estimation of location
(mean and mode) and scatter based on minimum spanning trees (pMST),
self-organizing maps (Flood Algorithm), Delaunay triangulations (RDELA),
and nested minimum volume convex sets (MVCH). The functions are also
suitable for outlier detection.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
