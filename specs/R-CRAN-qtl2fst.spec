%global __brp_check_rpaths %{nil}
%global packname  qtl2fst
%global packver   0.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.24
Release:          1%{?dist}%{?buildtag}
Summary:          Database Storage of Genotype Probabilities for QTL Mapping

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qtl2 >= 0.24
BuildRequires:    R-CRAN-fst 
Requires:         R-CRAN-qtl2 >= 0.24
Requires:         R-CRAN-fst 

%description
Uses the 'fst' package to store genotype probabilities on disk for the
'qtl2' package. These genotype probabilities are a central data object for
mapping quantitative trait loci (QTL), but they can be quite large. The
facilities in this package enable the genotype probabilities to be stored
on disk, leading to reduced memory usage with only a modest increase in
computation time.

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
