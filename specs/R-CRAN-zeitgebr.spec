%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  zeitgebr
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Circadian Behaviours

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-behavr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lomb 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-WaveletComp 
Requires:         R-CRAN-behavr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lomb 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-WaveletComp 

%description
Use behavioural variables to compute period, rhythmicity and other
circadian parameters. Methods include computation of chi square
periodograms (Sokolove and Bushell (1978)
<DOI:10.1016/0022-5193(78)90022-X>), Lomb-Scargle periodograms (Lomb
(1976) <DOI:10.1007/BF00648343>, Scargle (1982) <DOI:10.1086/160554>, Ruf
(1999) <DOI:10.1076/brhm.30.2.178.1422>), and autocorrelation-based
periodograms.

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
