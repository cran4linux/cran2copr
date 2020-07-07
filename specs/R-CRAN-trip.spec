%global packname  trip
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          2%{?dist}
Summary:          Tools for the Analysis of Animal Track Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-geodist 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-reproj 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-traipse 
BuildRequires:    R-CRAN-crsmeta 
Requires:         R-CRAN-geodist 
Requires:         R-CRAN-maptools 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-reproj 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-traipse 
Requires:         R-CRAN-crsmeta 

%description
Functions for accessing and manipulating spatial data for animal tracking,
with straightforward coercion from and to other formats. Filter for speed
and create time spent maps from animal track data. There are coercion
methods to convert between 'trip' and 'ltraj' from 'adehabitatLT', and
between 'trip' and 'psp' and 'ppp' from 'spatstat'. Trip objects can be
created from raw or grouped data frames, and from types in the 'sp', 'sf',
'amt', 'trackeR', 'mousetrap', and other packages.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/misc
%doc %{rlibdir}/%{packname}/ONEWS
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
