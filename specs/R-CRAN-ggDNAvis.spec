%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggDNAvis
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'ggplot2'-Based Tools for Visualising DNA Sequences and Modifications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 4.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggnewscale 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 4.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggnewscale 
Requires:         R-grid 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-png 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
Uses 'ggplot2' to visualise either (a) a single DNA/RNA sequence split
across multiple lines, (b) multiple DNA/RNA sequences, each occupying a
whole line, or (c) base modifications such as DNA methylation called by
modified bases models in Dorado or Guppy. Functions starting with
visualise_<>() are the main plotting functions, and functions starting
with extract_and_sort_<>() are key helper functions for reading files and
reformatting data. Source code is available at
<https://github.com/ejade42/ggDNAvis>, a full non-expert user guide is
available at <https://ejade42.github.io/ggDNAvis/>, and an interactive
web-app version of the software is available at
<https://ejade42.github.io/ggDNAvis/articles/interactive_app.html>.

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
