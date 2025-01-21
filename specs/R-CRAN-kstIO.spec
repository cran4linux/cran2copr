%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kstIO
%global packver   0.4-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Knowledge Space Theory Input/Output

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.4.0
Requires:         R-core >= 4.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pks >= 0.4.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-relations 
BuildRequires:    R-CRAN-kstMatrix 
Requires:         R-CRAN-pks >= 0.4.0
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-relations 
Requires:         R-CRAN-kstMatrix 

%description
Knowledge space theory by Doignon and Falmagne (1999)
<doi:10.1007/978-3-642-58625-5> is a set- and order-theoretical framework
which proposes mathematical formalisms to operationalize knowledge
structures in a particular domain.  The 'kstIO' package provides basic
functionalities to read and write KST data from/to files to be used
together with the 'kst', 'kstMatrix', 'CDSS', 'pks', or 'DAKS' packages.

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
