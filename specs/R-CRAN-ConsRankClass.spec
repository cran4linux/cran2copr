%global __brp_check_rpaths %{nil}
%global packname  ConsRankClass
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classification and Clustering of Preference Rankings

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ConsRank 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-proxy 
Requires:         R-CRAN-ConsRank 
Requires:         R-CRAN-janitor 
Requires:         R-methods 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-proxy 

%description
Tree-based classification and soft-clustering method for preference
rankings, with tools for external validation of fuzzy clustering. It
contains the recursive partitioning algorithm for preference rankings,
non-parametric tree-based method for a matrix of preference rankings as a
response variable. It contains also the distribution-free soft clustering
method for preference rankings, namely the K-median cluster component
analysis (CCA). The package depends on the 'ConsRank' R package. Options
for validate the tree-based method are both test-set procedure and V-fold
cross validation. The package contains the routines to compute the
adjusted concordance index (a fuzzy version of the adjusted rand index)
and the normalized degree of concordance (the corresponding fuzzy version
of the rand index). Essential references: D'Ambrosio, A., Amodio, S.,
Iorio, C., Pandolfo, G., and Siciliano, R. (2021)
<doi:10.1007/s00357-020-09367-0> D'Ambrosio, A., and Heiser, W.J. (2019)
<doi:10.1007/s41237-018-0069-5>; D'Ambrosio, A., and Heiser W.J. (2016)
<doi:10.1007/s11336-016-9505-1>; Hullermeier, E., Rifqi, M., Henzgen, S.,
and Senge, R. (2012) <doi:10.1109/TFUZZ.2011.2179303>.

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
