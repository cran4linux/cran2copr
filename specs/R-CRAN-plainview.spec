%global packname  plainview
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Plot Raster Images Interactively on a Plain HTML Canvas

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-methods 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-lattice 
Requires:         R-CRAN-png 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-viridisLite 

%description
Provides methods for plotting potentially large (raster) images
interactively on a plain HTML canvas. In contrast to package 'mapview'
data are plotted without background map, but data can be projected to any
spatial coordinate reference system. Supports plotting of classes
'RasterLayer', 'RasterStack', 'RasterBrick' (from package 'raster') as
well as 'png' files located on disk. Interactivity includes zooming,
panning, and mouse location information. In case of multi-layer
'RasterStacks' or 'RasterBricks', RGB image plots are created (similar to
'raster::plotRGB' - but interactive).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
