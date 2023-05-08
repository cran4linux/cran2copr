%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RNewsflow
%global packver   1.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Comparing Text Messages Across Time and Media

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-quanteda >= 3.2.3
BuildRequires:    R-CRAN-wordcloud >= 2.6
BuildRequires:    R-CRAN-stringi >= 1.7.8
BuildRequires:    R-CRAN-Matrix >= 1.5
BuildRequires:    R-CRAN-igraph >= 1.3.4
BuildRequires:    R-CRAN-scales >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.9
BuildRequires:    R-CRAN-RcppProgress >= 0.4.2
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.9.2
BuildRequires:    R-methods 
Requires:         R-CRAN-quanteda >= 3.2.3
Requires:         R-CRAN-wordcloud >= 2.6
Requires:         R-CRAN-stringi >= 1.7.8
Requires:         R-CRAN-Matrix >= 1.5
Requires:         R-CRAN-igraph >= 1.3.4
Requires:         R-CRAN-scales >= 1.2.1
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 1.0.9
Requires:         R-methods 

%description
A collection of tools for measuring the similarity of text messages and
tracing the flow of messages over time and across media.

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
