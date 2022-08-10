%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cassowaryr
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Scagnostics on Pairs of Numeric Variables in a Data Set

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-alphahull >= 2.5
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-splancs 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-energy 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-alphahull >= 2.5
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-splancs 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-energy 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-CRAN-tidyselect 

%description
Computes a range of scatterplot diagnostics (scagnostics) on pairs of
numerical variables in a data set. A range of scagnostics, including graph
and association-based scagnostics described by Leland Wilkinson and Graham
Wills (2008) <doi:10.1198/106186008X320465> and association-based
scagnostics described by Katrin Grimm (2016,ISBN:978-3-8439-3092-5) can be
computed. Summary and plotting functions are provided.

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
