%global __brp_check_rpaths %{nil}
%global packname  plothelper
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          New Plots Based on 'ggplot2' and Functions to Create RegularShapes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-ggfittext >= 0.8.1
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-farver 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-ggfittext >= 0.8.1
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magick 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-farver 

%description
An extension to 'ggplot2' and 'magick'. It contains three groups of
functions: Functions in the first group draw 'ggplot2' - based plots:
geom_shading_bar() draws barplot with shading colors in each bar.
geom_rect_cm(), geom_circle_cm() and geom_ellipse_cm() draw rectangles,
circles and ellipses with centimeter as their unit. Thus their sizes do
not change when the coordinate system or the aspect ratio changes.
annotation_transparent_text() draws labels with transparent texts.
annotation_shading_polygon() draws irregular polygons with shading colors.
Functions in the second group generate coordinates for regular shapes and
make linear transformations. Functions in the third group are 'magick' -
based functions facilitating image processing.

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
%{rlibdir}/%{packname}
