%global __brp_check_rpaths %{nil}
%global packname  spacejamr
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simulate Spatial Bernoulli Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-crsuggest 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-spatstat.random 
BuildRequires:    R-CRAN-spatstat.geom 
BuildRequires:    R-CRAN-ggthemes 
Requires:         R-CRAN-crsuggest 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-spatstat.random 
Requires:         R-CRAN-spatstat.geom 
Requires:         R-CRAN-ggthemes 

%description
Social network analysis is becoming commonplace in many social science
disciplines, but access to useful network data, especially among
marginalized populations, still remains a formidable challenge. This
package mitigates that problem by providing tools to simulate spatial
Bernoulli networks as proposed in Carter T. Butts (2002,
ISBN:978-0-493-72676-2), "Spatial models of large-scale interpersonal
networks." Using this package, network analysts can simulate a spatial
point process or sequence with a given number of nodes inside a
geographical boundary and estimate the probability of a tie formation
between all node pairs. When simulating a network, an analyst can choose
between five spatial interaction functions. The package also enables quick
comparison of summary statistics for simulated networks and provides
simple to use plotting methods for its classes that return plots which can
be further refined with the 'ggplot2' package.

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
