%global packname  sparrpowR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Power Analysis to Detect Spatial Relative Clusters

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sparr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-foreach 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sparr 
Requires:         R-stats 
Requires:         R-utils 

%description
Calculate the statistical power to detect clusters using kernel-based
spatial relative risk functions that are estimated using the 'sparr'
package. Details about the 'sparr' package methods can be found in the
tutorial: Davies et al. (2018) <doi:10.1002/sim.7577>.  Details about
kernel density estimation can be found in J. F. Bethell (1990)
<doi:10.1002/sim.4780090616>.  More information about relative risk
functions using kernel-density estimation can be found in J. F. Bithell
(1991) <doi:10.1002/sim.4780101112>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
