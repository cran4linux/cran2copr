%global packname  morphomap
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Morphometric Maps, Bone Landmarking and Cross Sectional Geometry

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-grDevices >= 3.5
BuildRequires:    R-graphics >= 3.5
BuildRequires:    R-CRAN-raster >= 3.0
BuildRequires:    R-CRAN-colorRamps >= 2.3
BuildRequires:    R-CRAN-Morpho >= 2.0
BuildRequires:    R-mgcv >= 1.8
BuildRequires:    R-CRAN-rgdal >= 1.4
BuildRequires:    R-CRAN-sp >= 1.3
BuildRequires:    R-CRAN-oce >= 1.1
BuildRequires:    R-CRAN-Arothron >= 1.0
BuildRequires:    R-CRAN-DescTools >= 0.99
BuildRequires:    R-CRAN-geometry >= 0.4.0
BuildRequires:    R-lattice >= 0.2
BuildRequires:    R-CRAN-Rvcg >= 0.18
BuildRequires:    R-CRAN-rgl >= 0.1
Requires:         R-grDevices >= 3.5
Requires:         R-graphics >= 3.5
Requires:         R-CRAN-raster >= 3.0
Requires:         R-CRAN-colorRamps >= 2.3
Requires:         R-CRAN-Morpho >= 2.0
Requires:         R-mgcv >= 1.8
Requires:         R-CRAN-rgdal >= 1.4
Requires:         R-CRAN-sp >= 1.3
Requires:         R-CRAN-oce >= 1.1
Requires:         R-CRAN-Arothron >= 1.0
Requires:         R-CRAN-DescTools >= 0.99
Requires:         R-CRAN-geometry >= 0.4.0
Requires:         R-lattice >= 0.2
Requires:         R-CRAN-Rvcg >= 0.18
Requires:         R-CRAN-rgl >= 0.1

%description
Extract cross sections from long bone meshes at specified intervals along
the diaphysis. Calculate two and three-dimensional morphometric maps,
cross-sectional geometric parameters, and semilandmarks on the periosteal
and endosteal contours of each cross section.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
