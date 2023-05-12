%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  corehunter
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Purpose Core Subset Selection

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-naturalsort >= 0.1.2
BuildRequires:    R-methods 
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-naturalsort >= 0.1.2
Requires:         R-methods 

%description
Core Hunter is a tool to sample diverse, representative subsets from large
germplasm collections, with minimum redundancy. Such so-called core
collections have applications in plant breeding and genetic resource
management in general. Core Hunter can construct cores based on genetic
marker data, phenotypic traits or precomputed distance matrices,
optimizing one of many provided evaluation measures depending on the
precise purpose of the core (e.g. high diversity, representativeness, or
allelic richness). In addition, multiple measures can be simultaneously
optimized as part of a weighted index to bring the different perspectives
closer together. The Core Hunter library is implemented in Java 8 as an
open source project (see <http://www.corehunter.org>).

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
