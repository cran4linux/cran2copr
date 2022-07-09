%global __brp_check_rpaths %{nil}
%global packname  Quartet
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Comparison of Phylogenetic Trees Using Quartet and Split Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-TreeTools >= 1.4.0
BuildRequires:    R-CRAN-Ternary >= 1.0
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-TreeTools >= 1.4.0
Requires:         R-CRAN-Ternary >= 1.0
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-ape 
Requires:         R-CRAN-viridisLite 

%description
Calculates the number of four-taxon subtrees consistent with a pair of
cladograms, calculating the symmetric quartet distance of Bandelt & Dress
(1986), Reconstructing the shape of a tree from observed dissimilarity
data, Advances in Applied Mathematics, 7, 309-343
<doi:10.1016/0196-8858(86)90038-2>, and using the tqDist algorithm of Sand
et al. (2014), tqDist: a library for computing the quartet and triplet
distances between binary or general trees, Bioinformatics, 30, 2079–2080
<doi:10.1093/bioinformatics/btu157> for pairs of binary trees.

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
