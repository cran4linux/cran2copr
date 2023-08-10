%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PLEXI
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multiplex Network Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-keras 
BuildRequires:    R-CRAN-ggraph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-aggregation 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-keras 
Requires:         R-CRAN-ggraph 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-aggregation 
Requires:         R-stats 
Requires:         R-graphics 

%description
Interactions between different biological entities are crucial for the
function of biological systems. In such networks, nodes represent
biological elements, such as genes, proteins and microbes, and their
interactions can be defined by edges, which can be either binary or
weighted. The dysregulation of these networks can be associated with
different clinical conditions such as diseases and response to treatments.
However, such variations often occur locally and do not concern the whole
network. To capture local variations of such networks, we propose
multiplex network differential analysis (MNDA). MNDA allows to quantify
the variations in the local neighborhood of each node (e.g. gene) between
the two given clinical states, and to test for statistical significance of
such variation. Yousefi et al. (2023) <doi:10.1101/2023.01.22.525058>.

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
