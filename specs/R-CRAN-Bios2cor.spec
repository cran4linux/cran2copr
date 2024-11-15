%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Bios2cor
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          From Biological Sequences and Simulations to Correlation Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-bio3d 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-bigmemory 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-bio3d 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-bigmemory 
Requires:         R-parallel 
Requires:         R-CRAN-igraph 

%description
Utilities for computation and analysis of correlation/covariation in
multiple sequence alignments and in side chain motions during molecular
dynamics simulations. Features include the computation of
correlation/covariation scores using a variety of scoring functions
between either sequence positions in alignments or side chain dihedral
angles in molecular dynamics simulations and utilities to analyze the
correlation/covariation matrix through a variety of tools including
network representation and principal components analysis. In addition,
several utility functions are based on the R graphical environment to
provide friendly tools for help in data interpretation. Examples of
sequence covariation analysis are provided in: (1) Pele J, Moreau M, Abdi
H, Rodien P, Castel H, Chabbert M (2014) <doi:10.1002/prot.24570> and (2)
Taddese B, Deniaud M, Garnier A, Tiss A, Guissouma H, Abdi H, Henrion D,
Chabbert M (2018) <doi:10.1371/journal.pcbi.1006209>. An example of side
chain correlated motion analysis is provided in: Taddese B, Garnier A,
Abdi H, Henrion D, Chabbert M (2020) <doi:10.1038/s41598-020-72766-1>.
This work was supported by the French National Research Agency (Grant
number: ANR-11-BSV2-026) and by GENCI (Grant number: 100567).

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
