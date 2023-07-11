%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BrailleR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Improved Access for Blind Users

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         python3dist(wxpython)
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-gridSVG 
BuildRequires:    R-CRAN-hunspell 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-quarto 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-roloc 
BuildRequires:    R-CRAN-rolocISCCNBS 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-gridSVG 
Requires:         R-CRAN-hunspell 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-mathjaxr 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-quarto 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-roloc 
Requires:         R-CRAN-rolocISCCNBS 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xtable 
Requires:         R-grDevices 

%description
Blind users do not have access to the graphical output from R without
printing the content of graphics windows to an embosser of some kind. This
is not as immediate as is required for efficient access to statistical
output.  The functions here are created so that blind people can make even
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
