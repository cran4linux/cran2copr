%global packname  RNewsflow
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Comparing Text Messages Across Time and Media

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-wordcloud 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-wordcloud 
Requires:         R-methods 
Requires:         R-CRAN-quanteda 

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
