%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  icons
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Insert SVG Icons into R Outputs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-cli 
Requires:         R-utils 
Requires:         R-CRAN-vctrs 

%description
Provides tools to download, style, and insert scalable vector graphics
(SVG) icons into R output, such as 'R Markdown' and 'Quarto' documents,
'Shiny' apps, 'gt' tables, and 'ggplot2' visualisations via the 'ggicons'
package. Bundles popular icon libraries, such as 'Font Awesome'
(<https://fontawesome.com>), 'Academicons'
(<https://jpswalsh.github.io/academicons/>), and 'Material Design Icons'
(<https://fonts.google.com/icons>), which are downloaded on demand to keep
the package small, or build a custom icon set from any folder of local SVG
files. Icon appearance, such as size, colour, and position, can be
customised.

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
