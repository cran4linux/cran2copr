%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  memery
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Internet Memes for Data Analysts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-Cairo 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-colourpicker 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-sysfonts 
Requires:         R-grid 
Requires:         R-CRAN-png 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-Cairo 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-colourpicker 

%description
Generates internet memes that optionally include a superimposed inset plot
and other atypical features, combining the visual impact of an
attention-grabbing meme with graphic results of data analysis. The package
differs from related packages that focus on imitating and reproducing
standard memes. Some packages do this by interfacing with online meme
generators whereas others achieve this natively. This package takes the
latter approach. It does not interface with online meme generators or
require any authentication with external websites. It reads images
directly from local files or via URL and meme generation is done by the
package. While this is similar to the 'meme' package available on CRAN, it
differs in that the focus is on allowing for non-standard meme layouts and
hybrids of memes mixed with graphs. While this package can be used to make
basic memes like an online meme generator would produce, it caters
primarily to hybrid graph-meme plots where the meme presentation can be
seen as a backdrop highlighting foreground graphs of data analysis
results. The package also provides support for an arbitrary number of meme
text labels with arbitrary size, position and other attributes rather than
restricting to the standard top and/or bottom text placement. This is
useful for proper aesthetic interleaving of plots of data between meme
image backgrounds and overlain text labels. The package offers a selection
of templates for graph placement and appearance with respect to the
underlying meme. Graph templates also permit additional template-specific
customization. Animated gif support is provided but this is optional and
functional only if the 'magick' package is installed. 'magick' is not
required unless gif functionality is desired.

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
