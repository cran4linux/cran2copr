%global packname  TexMix
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Supporting Functions and Data for Geo-Spatial Analytics Coursesat UTDallas, Texas

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-Formula 

%description
A collection of functions and data - mostly from Texas - is provided.
These are used as teaching tools for geo-spatial data analytics courses in
the GISciences program at The University of Texas at Dallas. In addition,
several vignettes illustrate geo-spatial data analytics practices, such as
relative risk kernel density estimations based on food store locations
within Dallas County or the identification of homogenous and spatially
contiguous market areas built on socio-economic, demographic and
infrastructure census information. The spatial resolution of the data-sets
ranges from 1623 food store locations, over geo-referenced areal data of
258 Texan counties, to 529 census tracts as well as 1669 block groups in
Dallas County. Cartographic, specialized regression and data handling
functions are provided.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
