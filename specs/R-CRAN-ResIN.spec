%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ResIN
%global packver   2.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Response Item Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-ggraph >= 2.2.0
BuildRequires:    R-CRAN-tidyr >= 1.3.0
BuildRequires:    R-CRAN-dplyr >= 1.1.3
BuildRequires:    R-CRAN-shadowtext >= 0.1.4
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-qgraph 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-wCorr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-DirectedClustering 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-CRAN-readr 
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-ggraph >= 2.2.0
Requires:         R-CRAN-tidyr >= 1.3.0
Requires:         R-CRAN-dplyr >= 1.1.3
Requires:         R-CRAN-shadowtext >= 0.1.4
Requires:         R-CRAN-psych 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-qgraph 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-wCorr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-DirectedClustering 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-parallelly 
Requires:         R-parallel 
Requires:         R-CRAN-doSNOW 
Requires:         R-CRAN-readr 

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
