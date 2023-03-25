%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  matrixcut
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Determines Clustering Threshold Based on Similarity Values

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-inflection 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-CRAN-inflection 

%description
The user must supply a matrix filled with similarity values. The software
will search for significant differences between similarity values at
different hierarchical levels. The algorithm will return a Loess-smoothed
plot of the similarity values along with the inflection point, if there
are any. There is the option to search for an inflection point within a
specified range. The package also has a function that will return the
matrix components at a specified cutoff. References: Mullner.
<ArXiv:1109.2378>; Cserhati, Carter. (2020, Journal of Creation
34(3):41-50),
<https://dl0.creation.com/articles/p137/c13759/j34-3_64-73.pdf>.

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
