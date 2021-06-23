%global __brp_check_rpaths %{nil}
%global packname  timsr
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Access timsTOF Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-opentimsr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-opentimsr 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
Access 'timsTOF' mass spectrometry data, as described
<https://sso.bruker.com/auth/realms/bruker/protocol/openid-connect/auth?client_id=aem-bruker.com&redirect_uri=https%%3A%%2F%%2Fwww.bruker.com%%2Fen.login.html%%3FtargetUrl%%3Dhttps%%3A%%2F%%2Fwww.bruker.com%%2Fen%%2Fservices%%2Fsoftware-downloads%%2Fmass-spectrometry.html&response_type=id_token%%20token&scope=openid%%20profile&state=4f9d225e92f341cca3b03a55533dbd65&nonce=f550633b1e984ecfb07979ae6d9277b4&ui_locales=en>
(after registering), using the 'OpenTIMS' C++ reader and save all into
'data.tables'.

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
