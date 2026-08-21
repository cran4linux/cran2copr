%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  themescopeR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Social Representation Analysis via Semantic Network Mapping

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-igraph >= 2.1.0
BuildRequires:    R-CRAN-Matrix >= 1.6.0
BuildRequires:    R-CRAN-dplyr >= 1.1.0
BuildRequires:    R-CRAN-ggrepel >= 0.9.0
BuildRequires:    R-CRAN-udpipe >= 0.8.11
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-igraph >= 2.1.0
Requires:         R-CRAN-Matrix >= 1.6.0
Requires:         R-CRAN-dplyr >= 1.1.0
Requires:         R-CRAN-ggrepel >= 0.9.0
Requires:         R-CRAN-udpipe >= 0.8.11
Requires:         R-methods 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Implements the ThemeScope framework for detecting and visualising social
representations in large-scale digital text corpora. From raw documents it
builds, via 'udpipe' annotation, sentence-level word co-occurrence
networks and derives two community-level indicators grounded in Social
Representation Theory: the Prototypical Salience Index (PSI) for anchoring
and the Concreteness Score (CS) for objectification. Communities are
located in a two-dimensional, theoretically grounded representational map.
The whole pipeline is usable from the R console; an optional 'shiny'
graphical interface calls the same exported functions. The method is
described in Misuraca, Spano and D'Aniello (2026)
<doi:10.1177/01655515261454276>.

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
