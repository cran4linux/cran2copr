%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  threeBrain
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Your Advanced 3D Brain Visualization

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.3.0
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-htmlwidgets >= 1.3
BuildRequires:    R-CRAN-shiny >= 1.2.0
BuildRequires:    R-CRAN-oro.nifti >= 0.9.1
BuildRequires:    R-CRAN-gifti >= 0.7.5
BuildRequires:    R-CRAN-digest >= 0.6.22
BuildRequires:    R-CRAN-freesurferformats >= 0.1.7
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-dipsaus 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-R6 >= 2.3.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-htmlwidgets >= 1.3
Requires:         R-CRAN-shiny >= 1.2.0
Requires:         R-CRAN-oro.nifti >= 0.9.1
Requires:         R-CRAN-gifti >= 0.7.5
Requires:         R-CRAN-digest >= 0.6.22
Requires:         R-CRAN-freesurferformats >= 0.1.7
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-dipsaus 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-png 
Requires:         R-CRAN-knitr 

%description
A fast, interactive cross-platform, and easy to share 'WebGL'-based 3D
brain viewer that visualizes 'FreeSurfer' and/or 'AFNI/SUMA' surfaces. The
viewer widget can be either standalone or embedded into 'R-shiny'
applications. The standalone version only require a web browser with
'WebGL2' support (for example, 'Chrome', 'Firefox', 'Safari'), and can be
inserted into any websites. The 'R-shiny' support allows the 3D viewer to
be dynamically generated from reactive user inputs. Please check the
publication by Wang, Magnotti, Zhang, and Beauchamp (2023,
<doi:10.1523/ENEURO.0328-23.2023>) for electrode localization. This viewer
has been fully adopted by 'RAVE' <https://openwetware.org/wiki/RAVE>, an
interactive toolbox to analyze 'iEEG' data by Magnotti, Wang, and
Beauchamp (2020, <doi:10.1016/j.neuroimage.2020.117341>). Please check
'citation("threeBrain")' for details.

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
