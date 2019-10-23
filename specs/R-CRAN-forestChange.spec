%global packname  forestChange
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Computing Essential Biodiversity Variables from Global ForestChange Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SDMTools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-parallel 
Requires:         R-CRAN-curl 
Requires:         R-graphics 
Requires:         R-CRAN-rvest 
Requires:         R-stats 
Requires:         R-CRAN-SDMTools 
Requires:         R-utils 
Requires:         R-CRAN-xml2 

%description
Metrics of two Essential Biodiversity Variables: forest extents and forest
fragmentation indices (O'connor et al., 2015) <doi:10.1002/rse2.4> are
computed by processing Global Forest Change data (Hansen et al., 2013)
<doi:10.1126/science.1244693>. The Forest Change Data are extracted using
either Geographic Administrative Units, see <https://gadm.org/>, or
user-defined polygons. Most of the procedures can be understood
implementing two functions: FCPolygon() and EBVmetric().

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rmd
%{rlibdir}/%{packname}/INDEX
