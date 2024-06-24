%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RMaCzek
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Czekanowski's Diagrams

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-GA >= 3.2
BuildRequires:    R-CRAN-seriation >= 1.3.4
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-ecp 
BuildRequires:    R-CRAN-FuzzyDBScan 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
Requires:         R-CRAN-GA >= 3.2
Requires:         R-CRAN-seriation >= 1.3.4
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-ecp 
Requires:         R-CRAN-FuzzyDBScan 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 

%description
Allows for production of Czekanowski's Diagrams with clusters. See K.
Bartoszek, A. Vasterlund (2020) <doi:10.2478/bile-2020-0008> and K.
Bartoszek, Y. Luo (2023) <doi:10.14708/ma.v51i2.7259>.

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
