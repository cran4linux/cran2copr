%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flows
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flow Matrix Selection with Statistics and Visualisation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mapsf 
BuildRequires:    R-CRAN-maplegend 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-CRAN-mapsf 
Requires:         R-CRAN-maplegend 
Requires:         R-utils 
Requires:         R-stats 

%description
The analysis and representation of flows often presuppose a selection to
facilitate interpretation. Various methods have been proposed for
selecting flows, one of the most widely used being based on major flows:
it selects only the most important flows, absolute or relative, on a local
or global scale. These methods often highlight hierarchies between
locations, but the loss of information caused by selection is rarely taken
into account. We propose statistical indicators to assess the loss of
information and the characteristics of selected flows. We provide
functions that select flows (main, dominant or major flows), provide
statistics on selections and offer visualizations in the form of maps and
graphs. See Beauguitte et al. (2015) <doi:10.4000/netcom.2134> for more
details.

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
