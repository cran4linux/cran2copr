%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tpn
%global packver   1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Truncated Positive Normal Model and Extensions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-skewMLRM 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-RBE3 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-skewMLRM 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-RBE3 

%description
Provide data generation and estimation tools for the truncated positive
normal (tpn) model discussed in Gomez, Olmos, Varela and Bolfarine (2018)
<doi:10.1007/s11766-018-3354-x>, the slash tpn distribution discussed in
Gomez, Gallardo and Santoro (2021) <doi:10.3390/sym13112164>, the bimodal
tpn distribution discussed in Gomez et al. (2022)
<doi:10.3390/sym14040665>, the flexible tpn model
<doi:10.3390/math11214431> and the unit tpn distribution
<doi:10.1016/j.chemolab.2025.105322>.

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
