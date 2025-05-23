%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cholera
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Amend, Augment and Aid Analysis of John Snow's Cholera Map

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-deldir >= 1.0.2
BuildRequires:    R-CRAN-HistData >= 0.7.8
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-elevatr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tanaka 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-threejs 
BuildRequires:    R-CRAN-TSP 
BuildRequires:    R-CRAN-viridisLite 
Requires:         R-CRAN-deldir >= 1.0.2
Requires:         R-CRAN-HistData >= 0.7.8
Requires:         R-CRAN-curl 
Requires:         R-CRAN-elevatr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tanaka 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-threejs 
Requires:         R-CRAN-TSP 
Requires:         R-CRAN-viridisLite 

%description
Amends errors, augments data and aids analysis of John Snow's map of the
1854 London cholera outbreak.

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
