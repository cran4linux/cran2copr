%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hightR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          HIGHT Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
HIGHT(HIGh security and light weigHT) algorithm is a block cipher
encryption algorithm developed to provide confidentiality in computing
environments that demand low power consumption and lightweight, such as
RFID(Radio-Frequency Identification) and USN(Ubiquitous Sensor Network),
or in mobile environments that require low power consumption and
lightweight, such as smartphones and smart cards. Additionally, it is
designed with a simple structure that enables it to be used with basic
arithmetic operations, XOR, and circular shifts in 8-bit units. This
algorithm was designed to consider both safety and efficiency in a very
simple structure suitable for limited environments, compared to the former
128-bit encryption algorithm SEED. In December 2010, it became an
ISO(International Organization for Standardization) standard. The detailed
procedure is described in Hong et al. (2006) <doi:10.1007/11894063_4>.

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
