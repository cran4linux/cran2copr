%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PANACEA
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Personalized Network-Based Anti-Cancer Therapy Evaluation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-reshape2 

%description
Identification of the most appropriate pharmacotherapy for each patient
based on genomic alterations is a major challenge in personalized
oncology. 'PANACEA' is a collection of personalized anti-cancer drug
prioritization approaches utilizing network methods. The methods utilize
personalized "driverness" scores from 'driveR' to rank drugs, mapping
these onto a protein-protein interaction network. The "distance-based"
method scores each drug based on these scores and distances between drugs
and genes to rank given drugs. The "RWR" method propagates these scores
via a random-walk with restart framework to rank the drugs. The methods
are described in detail in Ulgen E, Ozisik O, Sezerman OU. 2023. PANACEA:
network-based methods for pharmacotherapy prioritization in personalized
oncology. Bioinformatics <doi:10.1093/bioinformatics/btad022>.

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
