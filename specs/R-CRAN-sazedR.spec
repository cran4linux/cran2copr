%global packname  sazedR
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Parameter-Free Domain-Agnostic Season Length Detection in Time Series

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.1.4
BuildRequires:    R-CRAN-zoo >= 1.8.3
BuildRequires:    R-CRAN-bspec >= 1.5
BuildRequires:    R-CRAN-fftwtools >= 0.9.8
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-pracma >= 2.1.4
Requires:         R-CRAN-zoo >= 1.8.3
Requires:         R-CRAN-bspec >= 1.5
Requires:         R-CRAN-fftwtools >= 0.9.8
Requires:         R-CRAN-dplyr >= 0.8.0.1

%description
Spectral and Average Autocorrelation Zero Distance Density ('sazed') is a
method for estimating the season length of a seasonal time series. 'sazed'
is aimed at practitioners, as it employs only domain-agnostic
preprocessing and does not depend on parameter tuning or empirical
constants. The computation of 'sazed' relies on the efficient
autocorrelation computation methods suggested by Thibauld Nion (2012, URL:
<https://etudes.tibonihoo.net/literate_musing/autocorrelations.html>) and
by Bob Carpenter (2012, URL:
<https://lingpipe-blog.com/2012/06/08/autocorrelation-fft-kiss-eigen/>).

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
