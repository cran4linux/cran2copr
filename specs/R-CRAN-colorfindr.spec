%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  colorfindr
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Extract Colors from Windows BMP, JPEG, PNG, TIFF, and SVG Format Images

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-treemap 
BuildRequires:    R-CRAN-rsvg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-bmp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-plotwidgets 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-treemap 
Requires:         R-CRAN-rsvg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-bmp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-plotwidgets 

%description
Extracts colors from various image types, returns customized reports and
plots treemaps and 3D scatterplots of image compositions. Color palettes
can also be created.

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
