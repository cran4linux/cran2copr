%global __brp_check_rpaths %{nil}
%global packname  BrailleR
%global packver   0.32.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.32.1
Release:          1%{?dist}%{?buildtag}
Summary:          Improved Access for Blind Users

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3dist(wxpython) >= 4
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roloc 
BuildRequires:    R-CRAN-rolocISCCNBS 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roloc 
Requires:         R-CRAN-rolocISCCNBS 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 

%description
Blind users do not have access to the graphical output from R without
printing the content of graphics windows to an embosser of some kind. This
is not as immediate as is required for efficient access to statistical
output. The functions here are created so that blind people can make even
better use of R. This includes the text descriptions of graphs,
convenience functions to replace the functionality offered in many GUI
front ends, and experimental functionality for optimising graphical
content to prepare it for embossing as tactile images.

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
