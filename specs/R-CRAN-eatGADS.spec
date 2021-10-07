%global __brp_check_rpaths %{nil}
%global packname  eatGADS
%global packver   0.18.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.18.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Management of Large Hierarchical Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven >= 2.4.0
BuildRequires:    R-CRAN-eatDB >= 0.5.0
BuildRequires:    R-CRAN-eatTools >= 0.4.0
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-haven >= 2.4.0
Requires:         R-CRAN-eatDB >= 0.5.0
Requires:         R-CRAN-eatTools >= 0.4.0
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-hms 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringi 

%description
Import 'SPSS' data, handle and change 'SPSS' meta data, store and access
large hierarchical data in 'SQLite' data bases.

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
