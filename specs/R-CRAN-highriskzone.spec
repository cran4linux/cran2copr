%global packname  highriskzone
%global packver   1.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.5
Release:          1%{?dist}
Summary:          Determining and Evaluating High-Risk Zones

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat >= 1.54.0
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-maps 
Requires:         R-CRAN-spatstat >= 1.54.0
Requires:         R-CRAN-fields 
Requires:         R-CRAN-rgeos 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-deldir 
Requires:         R-Matrix 
Requires:         R-CRAN-maps 

%description
Functions for determining and evaluating high-risk zones and simulating
and thinning point process data, as described in 'Determining high risk
zones using point process methodology - Realization by building an R
package' Seibold (2012)
<http://highriskzone.r-forge.r-project.org/Bachelorarbeit.pdf> and
'Determining high-risk zones for unexploded World War II bombs by using
point process methodology', Mahling et al. (2013)
<doi:10.1111/j.1467-9876.2012.01055.x>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
