%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  leidenbase
%global packver   0.1.32
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.32
Release:          1%{?dist}%{?buildtag}
Summary:          R and C/C++ Wrappers to Run the Leiden find_partition() Function

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-igraph >= 0.9.0
Requires:         R-CRAN-igraph >= 0.9.0

%description
An R to C/C++ interface that runs the Leiden community detection algorithm
to find a basic partition (). It runs the equivalent of the 'leidenalg'
find_partition() function, which is given in the 'leidenalg' distribution
file 'leiden/src/functions.py'. This package includes the required source
code files from the official 'leidenalg' distribution and functions from
the R 'igraph' package.  The 'leidenalg' distribution is available from
<https://github.com/vtraag/leidenalg/> and the R 'igraph' package is
available from <https://igraph.org/r/>. The Leiden algorithm is described
in the article by Traag et al. (2019) <doi:10.1038/s41598-019-41695-z>.
Leidenbase includes code from the packages: igraph version 0.9.8 with
license GPL (>= 2), leidenalg version 0.8.10 with license GPL 3.

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
