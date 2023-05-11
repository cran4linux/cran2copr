%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ResIN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Response Item Networks ('ResIN')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.2
BuildRequires:    R-CRAN-wCorr >= 1.9.6
BuildRequires:    R-CRAN-qgraph >= 1.9.4
BuildRequires:    R-CRAN-fastDummies >= 1.6.3
BuildRequires:    R-CRAN-igraph >= 1.4.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-DirectedClustering >= 0.1.1
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-ggplot2 >= 3.4.2
Requires:         R-CRAN-wCorr >= 1.9.6
Requires:         R-CRAN-qgraph >= 1.9.4
Requires:         R-CRAN-fastDummies >= 1.6.3
Requires:         R-CRAN-igraph >= 1.4.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-DirectedClustering >= 0.1.1
Requires:         R-CRAN-Matrix 

%description
Contains various tools to perform and visualize Response Item Networks
('ResIN's'). 'ResIN' binarizes ordered-categorical and qualitative
response choices from (survey) data, calculates pairwise associations and
maps the location of each item response as a node in a force-directed
network. Please refer to <https://www.resinmethod.net/> for more details.

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
