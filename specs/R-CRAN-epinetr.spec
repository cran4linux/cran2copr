%global packname  epinetr
%global packver   0.93
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.93
Release:          1%{?dist}%{?buildtag}
Summary:          Epistatic Network Modelling with Forward-Time Simulation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-GA >= 3.2
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-RcppAlgos >= 2.4.1
BuildRequires:    R-methods >= 2.10
BuildRequires:    R-CRAN-vcfR >= 1.8.0
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-GA >= 3.2
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-RcppAlgos >= 2.4.1
Requires:         R-methods >= 2.10
Requires:         R-CRAN-vcfR >= 1.8.0
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-CRAN-Rcpp >= 0.12.18

%description
Allows for forward-in-time simulation of epistatic networks with
associated phenotypic output.

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
