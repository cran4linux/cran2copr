%global packname  hydraulics
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Basic Pipe Hydraulics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-reshape2 

%description
Functions for basic hydraulic calculations related to water flow in
circular pipes flowing full (under pressure). This includes friction loss
calculations by solving the Darcy-Weisbach equation for head loss, flow or
diameter, and plotting a Moody diagram. The Darcy-Weisbach friction factor
is calculated using the Colebrook (or Colebrook-White equation), the basis
of the Moody diagram, the original citation being Colebrook (1939)
<doi:10.1680/ijoti.1939.13150>. The derivation of the Darcy-Weisbach
equation and methods for its solution are outlined in many fluid mechanics
texts such as Finnemore and Franzini (2002, ISBN:978-0072432022). This
package is designed to work similarly to the 'iemisc' package, but with an
emphasis on pipe flow.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
