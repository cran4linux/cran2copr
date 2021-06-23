%global __brp_check_rpaths %{nil}
%global packname  lconnect
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simple Tools to Compute Landscape Connectivity Metrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-igraph 

%description
Provides functions to upload vectorial data and derive landscape
connectivity metrics in habitat or matrix systems. Additionally, includes
an approach to assess individual patch contribution to the overall
landscape connectivity, enabling the prioritization of habitat patches.
The computation of landscape connectivity and patch importance are very
useful in Landscape Ecology research. The metrics available are: number of
components, number of links, size of the largest component, mean size of
components, class coincidence probability, landscape coincidence
probability, characteristic path length, expected cluster size,
area-weighted flux and integral index of connectivity. Pascual-Hortal, L.,
and Saura, S. (2006) <doi:10.1007/s10980-006-0013-z> Urban, D., and Keitt,
T. (2001) <doi:10.2307/2679983> Laita, A., Kotiaho, J., Monkkonen, M.
(2011) <doi:10.1007/s10980-011-9620-4>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
