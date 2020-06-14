%global packname  gridSVG
%global packver   1.7-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          2%{?dist}
Summary:          Export 'grid' Graphics as SVG

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-XML 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-XML 

%description
Functions to export graphics drawn with package grid to SVG format.
Additional functions provide access to SVG features that are not available
in standard R graphics, such as hyperlinks, animation, filters, masks,
clipping paths, and gradient and pattern fills.

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
%doc %{rlibdir}/%{packname}/js
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/svg
%{rlibdir}/%{packname}/INDEX
