%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dupNodes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Creates an 'igraph' Object that Duplicates Nodes with Self-Loops

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-dogesr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-dogesr 

%description
Creates a new graph from an existing one, duplicating nodes with
self-loops. This can be used for a computation of betweenness centrality
that does not drop this essential information. Implements Merelo &
Molinari (2021) <doi:10.1007/s42001-023-00245-4>.

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
