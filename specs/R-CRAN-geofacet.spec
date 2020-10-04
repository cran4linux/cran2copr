%global packname  geofacet
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          'ggplot2' Faceting Utilities for Geographical Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rnaturalearth 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-imguR 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-geogrid 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-gtable 
Requires:         R-graphics 
Requires:         R-CRAN-rnaturalearth 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-imguR 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-geogrid 
Requires:         R-methods 

%description
Provides geofaceting functionality for 'ggplot2'. Geofaceting arranges a
sequence of plots of data for different geographical entities into a grid
that preserves some of the geographical orientation.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
