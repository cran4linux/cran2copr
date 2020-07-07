%global packname  barsurf
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}
Summary:          Heatmap-Related Plots and Smooth Multiband Color Interpolation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-kubik 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-CRAN-kubik 
Requires:         R-CRAN-colorspace 

%description
Supports combined contour-heat plots and 3D bar/surface plots, for
plotting scalar fields, either discretely-spaced or continuously-spaced.
Also, supports matrix visualization (per se), isosurfaces (for scalar
fields over three variables), triangular plots and vector fields. All
plots use static vector graphics (suitable for Sweave documents), but high
resolution heatmaps can produce smooth raster-like visual effects.
Contains a flexible system for smooth multiband color interpolation in
RGB, HSV and HCL color spaces.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
