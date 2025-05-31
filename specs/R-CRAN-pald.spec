%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pald
%global packver   0.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Partitioned Local Depth for Community Structure in Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-CRAN-glue 

%description
Implementation of the Partitioned Local Depth (PaLD) approach which
provides a measure of local depth and the cohesion of a point to another
which (together with a universal threshold for distinguishing strong and
weak ties) may be used to reveal local and global structure in data, based
on methods described in Berenhaut, Moore, and Melvin (2022)
<doi:10.1073/pnas.2003634119>. No extraneous inputs, distributional
assumptions, iterative procedures nor optimization criteria are employed.
This package includes functions for computing local depths and cohesion as
well as flexible functions for plotting community networks and displays of
cohesion against distance.

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
