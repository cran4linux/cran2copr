%global packname  RadData
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Nuclear Decay Data for Dosimetric Calculations - ICRP 107

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Nuclear Decay Data for Dosimetric Calculations from the International
Commission on Radiological Protection from ICRP Publication 107. Ann. ICRP
38 (3). Eckerman, Keith and Endo, Akira 2008
<doi:10.1016/j.icrp.2008.10.004>
<https://www.icrp.org/publication.asp?id=ICRP%%20Publication%%20107>. This
is a database of the physical data needed in calculations of
radionuclide-specific protection and operational quantities. The data is
prescribed by the ICRP, the international authority on radiation dose
standards, for estimating dose from the intake of or exposure to
radionuclides in the workplace and the environment. The database contains
information on the half-lives, decay chains, and yields and energies of
radiations emitted in nuclear transformations of 1252 radionuclides of 97
elements.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
