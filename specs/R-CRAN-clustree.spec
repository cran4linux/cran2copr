%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clustree
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Visualise Clusterings at Different Resolutions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidygraph 
BuildRequires:    R-CRAN-ggrepel 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-dplyr 
Requires:         R-grid 
Requires:         R-CRAN-viridis 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidygraph 
Requires:         R-CRAN-ggrepel 

%description
Deciding what resolution to use can be a difficult question when
approaching a clustering analysis. One way to approach this problem is to
look at how samples move as the number of clusters increases. This package
allows you to produce clustering trees, a visualisation for interrogating
clusterings as resolution increases.

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
