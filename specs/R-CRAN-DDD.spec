%global packname  DDD
%global packver   4.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Diversity-Dependent Diversification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-SparseM 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-SparseM 

%description
Implements maximum likelihood and bootstrap methods based on the
diversity-dependent birth-death process to test whether speciation or
extinction are diversity-dependent, under various models including various
types of key innovations. See Etienne et al. 2012, Proc. Roy. Soc. B 279:
1300-1309, <DOI:10.1098/rspb.2011.1439>, Etienne & Haegeman 2012, Am. Nat.
180: E75-E89, <DOI:10.1086/667574> and Etienne et al. 2016. Meth. Ecol.
Evol. 7: 1092-1099, <DOI:10.1111/2041-210X.12565>. Also contains functions
to simulate the diversity-dependent process.

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
