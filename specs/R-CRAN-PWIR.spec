%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PWIR
%global packver   0.0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Provides a Function to Calculate Prize Winner Indices Based on Bibliometric Data

License:          EUPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-bibliometrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-progressr 
Requires:         R-CRAN-bibliometrix 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-progressr 

%description
A function 'PWI()' that calculates prize winner indices based on
bibliometric data is provided. The default is the 'Derek de Solla Price
Memorial Medal'. Users can provide recipients of other prizes.

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
