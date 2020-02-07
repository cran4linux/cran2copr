%global packname  sampSurf
%global packver   0.7-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          Sampling Surface Simulation for Areal Sampling Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster >= 2.9.5
BuildRequires:    R-boot >= 1.3.3
BuildRequires:    R-CRAN-sp >= 1.3.0
BuildRequires:    R-CRAN-latticeExtra >= 0.6.28
BuildRequires:    R-CRAN-rasterVis >= 0.45
BuildRequires:    R-lattice >= 0.20.35
BuildRequires:    R-methods 
Requires:         R-CRAN-raster >= 2.9.5
Requires:         R-boot >= 1.3.3
Requires:         R-CRAN-sp >= 1.3.0
Requires:         R-CRAN-latticeExtra >= 0.6.28
Requires:         R-CRAN-rasterVis >= 0.45
Requires:         R-lattice >= 0.20.35
Requires:         R-methods 

%description
Sampling surface simulation is useful in the comparison of different areal
sampling methods in forestry, ecology and natural resources. The sampSurf
package allows the simulation of numerous sampling methods for standing
trees and downed woody debris in a spatial context. It also provides an S4
class and method structure that facilitates the addition of new sampling
methods.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
