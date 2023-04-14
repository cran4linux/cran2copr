%global __brp_check_rpaths %{nil}
%global packname  soiltexture
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Functions for Soil Texture Plot, Classification andTransformation

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-MASS 
BuildRequires:    R-tools 
BuildRequires:    R-tcltk 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp 
Requires:         R-MASS 
Requires:         R-tools 
Requires:         R-tcltk 
Requires:         R-utils 

%description
"The Soil Texture Wizard" is a set of R functions designed to produce
texture triangles (also called texture plots, texture diagrams, texture
ternary plots), classify and transform soil textures data. These functions
virtually allows to plot any soil texture triangle (classification) into
any triangle geometry (isosceles, right-angled triangles, etc.). This set
of function is expected to be useful to people using soil textures data
from different soil texture classification or different particle size
systems. Many (> 15) texture triangles from all around the world are
predefined in the package. A simple text based graphical user interface is
provided: soiltexture_gui().

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
