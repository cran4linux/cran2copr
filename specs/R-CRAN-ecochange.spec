%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecochange
%global packver   2.9.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.9.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Integrating Ecosystem Remote Sensing Products to Derive EBV Indicators

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rasterVis 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-landscapemetrics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-rasterDT 
BuildRequires:    R-stats 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-parallel 
Requires:         R-CRAN-rasterVis 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-landscapemetrics 
Requires:         R-CRAN-tibble 
Requires:         R-utils 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-getPass 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-rasterDT 
Requires:         R-stats 

%description
Essential Biodiversity Variables (EBV) are state variables with dimensions
on time, space, and biological organization that document biodiversity
change. Freely available ecosystem remote sensing products (ERSP) are
downloaded and integrated with data for national or regional domains to
derive indicators for EBV in the class ecosystem structure (Pereira et
al., 2013) <doi:10.1126/science.1229931>, including horizontal ecosystem
extents, fragmentation, and information-theory indices. To process ERSP,
users must provide a polygon or geographic administrative data map.
Downloadable ERSP include Global Surface Water (Peckel et al., 2016)
<doi:10.1038/nature20584>, Forest Change (Hansen et al., 2013)
<doi:10.1126/science.1244693>, and Continuous Tree Cover data (Sexton et
al., 2013) <doi:10.1080/17538947.2013.786146>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
