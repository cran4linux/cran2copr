%global packname  quadmesh
%global packver   0.4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          3%{?dist}
Summary:          Quadrangle Mesh

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-reproj >= 0.4.0
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gridBase 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-reproj >= 0.4.0
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gridBase 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-png 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-scales 

%description
Create surface forms from matrix or 'raster' data for flexible plotting
and conversion to other mesh types. The functions 'quadmesh' or
'triangmesh' produce a continuous surface as a 'mesh3d' object as used by
the 'rgl' package. This is used for plotting raster data in 3D (optionally
with texture), and allows the application of a map projection without data
loss and many processing applications that are restricted by inflexible
regular grid rasters. There are discrete forms of these continuous
surfaces available with 'dquadmesh' and 'dtriangmesh' functions.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
