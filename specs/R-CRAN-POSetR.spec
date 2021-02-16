%global packname  POSetR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Partially Ordered Sets in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-CRAN-Rdpack 

%description
Provides a set of basic tools for generating, analyzing, summarizing and
visualizing finite partially ordered sets. In particular, it implements
flexible and very efficient algorithms for the extraction of linear
extensions and for the computation of mutual ranking probabilities and
other user-defined functionals, over them. The package is meant as a
computationally efficient "engine", for the implementation of data
analysis procedures, on systems of multidimensional ordinal indicators and
partially ordered data, in the spirit of Fattore, M. (2016) "Partially
ordered sets and the measurement of multidimensional ordinal deprivation",
Social Indicators Research <DOI:10.1007/s11205-015-1059-6>, and Fattore M.
and Arcagni, A. (2018) "A reduced posetic approach to the measurement of
multidimensional ordinal deprivation", Social Indicators Research
<DOI:10.1007/s11205-016-1501-4>.

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
