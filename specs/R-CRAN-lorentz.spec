%global packname  lorentz
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          The Lorentz Transform in Relativistic Physics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-emulator >= 1.2.20
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-emulator >= 1.2.20
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tensor 

%description
The Lorentz transform in special relativity; also the gyrogroup structure
of three-velocities following Ungar (2006)
<doi:10.1088/0143-0807/27/3/L02>.  For general relativity, see the
'schwarzschild' package.

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
%doc %{rlibdir}/%{packname}/3dplotting.R
%doc %{rlibdir}/%{packname}/distributive_search.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/lorentz_noncommutative.svg
%doc %{rlibdir}/%{packname}/nondistributive_plotter.R
%doc %{rlibdir}/%{packname}/video.R
%{rlibdir}/%{packname}/INDEX
