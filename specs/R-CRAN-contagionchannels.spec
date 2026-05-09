%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  contagionchannels
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Stage Detection and Attribution of Cross-Border Financial Contagion Channels

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-waveslim 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-waveslim 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of a two-stage framework for the joint
detection-and-attribution of cross-border financial contagion. Stage one
detects directional information flows between equity markets via
Wavelet-Quantile Transfer Entropy, combining maximal-overlap discrete
wavelet decomposition (Percival and Walden, 2000, ISBN:9780521685085) with
the transfer-entropy estimator of Schreiber (2000)
<doi:10.1103/PhysRevLett.85.461> and quantile conditioning following Han,
Linton, Oka and Whang (2016) <doi:10.1016/j.jeconom.2016.03.001>. Stage
two attributes each significant directional link to one of five mutually
exclusive transmission channels (Trade, Financial, Geopolitical,
Behavioural, Monetary Policy) through a multi-method structural
identification architecture combining instrumental-variables two-stage
least squares with channel-specific external instruments (Stock and
Watson, 2018) <doi:10.1111/ecoj.12593>, LASSO-based instrument selection
(Belloni, Chernozhukov and Hansen, 2014) <doi:10.1093/restud/rdt044>,
local projections (Jorda, 2005) <doi:10.1257/0002828053828518>,
heteroskedasticity-based identification (Rigobon, 2003)
<doi:10.1162/003465303772815727>, and the Cinelli-Hazlett (2020)
<doi:10.1111/rssb.12348> robustness-value sensitivity bound. Bundled
datasets and replication scripts reproduce the headline findings of
Bhandari, Parida and Sahu (2026) <doi:10.48550/arXiv.2604.26546>; the
package is general-purpose and accommodates user-supplied returns and
channel proxies.

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
