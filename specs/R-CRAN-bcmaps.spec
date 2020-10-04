%global packname  bcmaps
%global packver   0.18.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.18.1
Release:          3%{?dist}%{?buildtag}
Summary:          Map Layers and Spatial Utilities for British Columbia

License:          Apache License (== 2.0) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-sf >= 0.9
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-sf >= 0.9
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides access to various spatial layers for B.C., such as administrative
boundaries, natural resource management boundaries, etc. All layers are
imported from the 'bcmapsdata' package as 'sf' or 'Spatial' objects
through function calls in this package. All layers are in B.C. 'Albers'
equal-area projection
<http://spatialreference.org/ref/epsg/nad83-bc-albers/>, which is the B.C.
government standard.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
