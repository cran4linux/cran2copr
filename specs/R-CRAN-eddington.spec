%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eddington
%global packver   4.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Compute a Cyclist's Eddington Number

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-R6 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-XML 

%description
Compute a cyclist's Eddington number, including efficiently computing
cumulative E over a vector. A cyclist's Eddington number
<https://en.wikipedia.org/wiki/Arthur_Eddington#Eddington_number_for_cycling>
is the maximum number satisfying the condition such that a cyclist has
ridden E miles or greater on E distinct days. The algorithm in this
package is an improvement over the conventional approach because both
summary statistics and cumulative statistics can be computed in linear
time, since it does not require initial sorting of the data. These
functions may also be used for computing h-indices for authors, a metric
described by Hirsch (2005) <doi:10.1073/pnas.0507655102>. Both are
specific applications of computing the side length of a Durfee square
<https://en.wikipedia.org/wiki/Durfee_square>.

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
