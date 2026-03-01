%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RGraphSpace
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Lightweight Interface Between 'igraph' and 'ggplot2' Graphics

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4
Requires:         R-core >= 4.4
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggrastr 
BuildRequires:    R-CRAN-circlize 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-scales 
Requires:         R-grid 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggrastr 
Requires:         R-CRAN-circlize 

%description
Interface to integrate 'igraph' and 'ggplot2' graphics in a normalized
coordinate system. 'RGraphSpace' implements new geometric objects using
'ggplot2' prototypes, customized for side-by-side visualization of
multiple graphs. By scaling shapes and graph elements, 'RGraphSpace' helps
to create layered visualizations that stay coherent across multiple
graphs.

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
