%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  partykit
%global packver   1.2-21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.21
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Recursive Partytioning

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-rpart >= 4.1.11
BuildRequires:    R-CRAN-Formula >= 1.2.1
BuildRequires:    R-CRAN-libcoin >= 1.0.0
BuildRequires:    R-CRAN-inum >= 1.0.0
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-rpart >= 4.1.11
Requires:         R-CRAN-Formula >= 1.2.1
Requires:         R-CRAN-libcoin >= 1.0.0
Requires:         R-CRAN-inum >= 1.0.0
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-mvtnorm 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-survival 

%description
A toolkit with infrastructure for representing, summarizing, and
visualizing tree-structured regression and classification models. This
unified infrastructure can be used for reading/coercing tree models from
different sources ('rpart', 'RWeka', 'PMML') yielding objects that share
functionality for print()/plot()/predict() methods. Furthermore, new and
improved reimplementations of conditional inference trees (ctree()) and
model-based recursive partitioning (mob()) from the 'party' package are
provided based on the new infrastructure. A description of this package
was published by Hothorn and Zeileis (2015)
<https://jmlr.org/papers/v16/hothorn15a.html>.

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
