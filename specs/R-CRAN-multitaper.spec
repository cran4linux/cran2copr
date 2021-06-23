%global __brp_check_rpaths %{nil}
%global packname  multitaper
%global packver   1.0-15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.15
Release:          1%{?dist}%{?buildtag}
Summary:          Spectral Analysis Tools using the Multitaper Method

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Implements multitaper spectral analysis using discrete prolate spheroidal
sequences (Slepians) and sine tapers. It includes an adaptive weighted
multitaper spectral estimate, a coherence estimate, Thomson's Harmonic
F-test, and complex demodulation. The Slepians sequences are generated
efficiently using a tridiagonal matrix solution, and jackknifed confidence
intervals are available for most estimates. This package is an
implementation of the method described in D.J. Thomson (1982) "Spectrum
estimation and harmonic analysis" <doi:10.1109/PROC.1982.12433>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
