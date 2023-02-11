%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  trtf
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Transformation Trees and Forests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mlt >= 1.4.1
BuildRequires:    R-CRAN-partykit >= 1.2.1
BuildRequires:    R-CRAN-tram 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-CRAN-libcoin 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-mlt >= 1.4.1
Requires:         R-CRAN-partykit >= 1.2.1
Requires:         R-CRAN-tram 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-sandwich 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-variables 
Requires:         R-CRAN-libcoin 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Recursive partytioning of transformation models with corresponding random
forest for conditional transformation models as described in
'Transformation Forests' (Hothorn and Zeileis, 2021,
<doi:10.1080/10618600.2021.1872581>) and 'Top-Down Transformation Choice'
(Hothorn, 2018, <DOI:10.1177/1471082X17748081>).

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
