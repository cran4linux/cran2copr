%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  texPreview
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compile and Preview Snippets of 'LaTeX'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       tex(standalone.cls)
BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-details 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-svgPanZoom 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-tinytex 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-details 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-rematch2 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-svgPanZoom 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-tinytex 

%description
Compile snippets of 'LaTeX' directly into images from the R console to
view in the 'RStudio' viewer pane, Shiny apps and 'RMarkdown' documents.

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
