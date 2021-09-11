%global __brp_check_rpaths %{nil}
%global packname  edmcr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Euclidean Distance Matrix Completion Tools

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-lbfgs 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-sdpt3r 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-lbfgs 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-sdpt3r 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-stats 

%description
Implements various general algorithms to estimate missing elements of a
Euclidean (squared) distance matrix. Includes optimization methods based
on semi-definite programming found in Alfakih, Khadani, and Wolkowicz
(1999)<doi:10.1023/A:1008655427845>, a non-convex position formulation by
Fang and O'Leary (2012)<doi:10.1080/10556788.2011.643888>, and a
dissimilarity parameterization formulation by Trosset
(2000)<doi:10.1023/A:1008722907820>. When the only non-missing distances
are those on the minimal spanning tree, the guided random search algorithm
will complete the matrix while preserving the minimal spanning tree
following Rahman and Oldford (2018)<doi:10.1137/16M1092350>. Point
configurations in specified dimensions can be determined from the
completions. Special problems such as the sensor localization problem, as
for example in Krislock and Wolkowicz (2010)<doi:10.1137/090759392>, as
well as reconstructing the geometry of a molecular structure, as for
example in Hendrickson (1995)<doi:10.1137/0805040>, can also be solved.
These and other methods are described in the thesis of Adam
Rahman(2018)<https://hdl.handle.net/10012/13365>.

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
