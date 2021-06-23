%global __brp_check_rpaths %{nil}
%global packname  geotopbricks
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          3%{?dist}%{?buildtag}
Summary:          An R Plug-in for the Distributed Hydrological Model GEOtop

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-rgdal 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-rgdal 

%description
It analyzes raster maps and other information as input/output files from
the Hydrological Distributed Model GEOtop. It contains functions and
methods to import maps and other keywords from geotop.inpts file. Some
examples with simulation cases of GEOtop 2.x/3.x are presented in the
package. Any information about the GEOtop Distributed Hydrological Model
source code is available on www.geotop.org. Technical details about the
model are available in Endrizzi et al, 2014
(<http://www.geosci-model-dev.net/7/2831/2014/gmd-7-2831-2014.html>).

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
%doc %{rlibdir}/%{packname}/brick3DTensor-test
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/geotopbricks-manual.pdf
%doc %{rlibdir}/%{packname}/regression-testing
%doc %{rlibdir}/%{packname}/rendena100
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
