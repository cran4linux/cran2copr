%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LISTO
%global packver   0.7.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.3
Release:          1%{?dist}%{?buildtag}
Summary:          Performing Comprehensive Overlap Assessments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-primes 
BuildRequires:    R-CRAN-statisfactory 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-primes 
Requires:         R-CRAN-statisfactory 
Requires:         R-stats 

%description
The implementation of a statistical framework for performing overlap
assessments on lists comprising sets of strings (such as lists of gene
sets) described in Stoica (2023)
<https://ora.ox.ac.uk/objects/uuid:b0847284-a02f-47ee-88e3-a3c4e0cdb8b1>.
It can assess overlaps of pairs of sets of strings selected either from
the same universe or from different universes, and overlaps of triplets of
sets of strings selected from the same universe. Designed for single-cell
RNA-sequencing data analysis applications, but suitable for other purposes
as well.

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
