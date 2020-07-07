%global packname  eChem
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Simulations for Electrochemistry Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-animation 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-animation 

%description
Simulates cyclic voltammetry, linear-sweep voltammetry (both with and
without stirring of the solution), and single-pulse and double-pulse
chronoamperometry and chronocoulometry experiments using the implicit
finite difference method outlined in Gosser (1993, ISBN: 9781560810261)
and in Brown (2015) <doi:10.1021/acs.jchemed.5b00225>. Additional
functions provide ways to display and to examine the results of these
simulations. The primary purpose of this package is to provide tools for
use in courses in analytical chemistry.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
