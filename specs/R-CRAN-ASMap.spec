%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ASMap
%global packver   1.0-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Linkage Map Construction using the MSTmap Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gtools 

%description
Functions for Accurate and Speedy linkage map construction, manipulation
and diagnosis of Doubled Haploid, Backcross and Recombinant Inbred 'R/qtl'
objects. This includes extremely fast linkage map clustering and optimal
marker ordering using 'MSTmap' (see Wu et al.,2008).

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
