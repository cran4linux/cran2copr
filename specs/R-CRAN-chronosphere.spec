%global packname  chronosphere
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Earth System History Variables

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-utils 

%description
The purpose of the 'chronosphere' project is to facilitate spatially
explicit analyses of (paleo)environmental/ecological research. The package
serves as a gateway to plate tectonic reconstructions, deep time global
climate model results as well as fossil occurrence datasets such as the
Paleobiology Database <https://paleobiodb.org/> and the PaleoReefs
Database <https://www.paleo-reefs.pal.uni-erlangen.de/>. Environmental
data stored on a remote server can be downloaded and imported directly to
the R environment. Query functions to the GPlates
<https://www.gplates.org/> desktop application or the GPlates Web Service
<https://gws.gplates.org/> allow users to reconstruct coordinates, static
plates, and Spatial objects. A wrapper class 'RasterArray' is implemented
around the 'RasterLayer' class, allowing the organization of spatially
explicit raster data in n-dimensional arrays. The project is developed
under the umbrella of the DFG (Deutsche Forschungsgemeinschaft) Research
Unit TERSANE2 (For 2332, TEmperature Related Stressors in ANcient
Extinctions).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
