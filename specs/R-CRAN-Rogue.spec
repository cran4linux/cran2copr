%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rogue
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Identify Rogue Taxa in Sets of Phylogenetic Trees

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-CRAN-cli >= 3.0
BuildRequires:    R-CRAN-TreeTools >= 1.6.0.9007
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-TreeDist > 2.2.0
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-CRAN-cli >= 3.0
Requires:         R-CRAN-TreeTools >= 1.6.0.9007
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-TreeDist > 2.2.0
Requires:         R-CRAN-fastmatch 
Requires:         R-grDevices 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 
Requires:         R-utils 

%description
Rogue ("wildcard") taxa are leaves with uncertain phylogenetic position.
Their position may vary from tree to tree under inference methods that
yield a tree set (e.g. bootstrapping, Bayesian tree searches, maximum
parsimony). The presence of rogue taxa in a tree set can potentially
remove all information from a consensus tree. The information content of a
consensus tree - a function of its resolution and branch support values -
can often be increased by removing rogue taxa. 'Rogue' provides an
explicitly information-theoretic approach to rogue detection (Smith 2022)
<doi:10.1093/sysbio/syab099>, and an interface to 'RogueNaRok' (Aberer et
al. 2013) <doi:10.1093/sysbio/sys078>.

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
