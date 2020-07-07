%global packname  circlize
%global packver   0.4.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.10
Release:          2%{?dist}
Summary:          Circular Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-GlobalOptions >= 0.1.2
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-shape 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
Requires:         R-CRAN-GlobalOptions >= 0.1.2
Requires:         R-graphics 
Requires:         R-CRAN-shape 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-grid 

%description
Circular layout is an efficient way for the visualization of huge amounts
of information. Here this package provides an implementation of circular
layout generation in R as well as an enhancement of available software.
The flexibility of the package is based on the usage of low-level graphics
functions such that self-defined high-level graphics can be easily
implemented by users for specific purposes. Together with the seamless
connection between the powerful computational and visual environment in R,
it gives users more convenience and freedom to design figures for better
understanding complex patterns behind multiple dimensional data. The
package is described in Gu et al. 2014
<doi:10.1093/bioinformatics/btu393>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
