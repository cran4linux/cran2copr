%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IndexConstruction
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Index Construction for Time Series Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-fGarch 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-RcppBDT 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-fGarch 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-RcppBDT 
Requires:         R-CRAN-zoo 

%description
Derivation of indexes for benchmarking purposes. A methodology with
flexible number of constituents is implemented. Also functions for market
capitalization and volume weighted indexes with fixed number of
constituents are available. The main function of the package, indexComp(),
provides the derived index, suitable for analysis purposes. The functions
indexUpdate(), indexMemberSelection() and indexMembersUpdate() are
components of indexComp() and enable one to construct and continuously
update an index, e.g. for display on a website. The methodology behind the
functions provided gets introduced in Trimborn and Haerdle (2018)
<doi:10.1016/j.jempfin.2018.08.004>.

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
