%global packname  yaps
%global packver   1.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.4
Release:          1%{?dist}%{?buildtag}
Summary:          Track Estimation using YAPS (Yet Another Positioning Solver)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-splusTimeSeries 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-TMB 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-splusTimeSeries 
Requires:         R-stats 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-TMB 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-zoo 

%description
Estimate tracks of animals tagged with acoustic transmitters. 'yaps' was
introduced in 2017 as a transparent open-source tool to estimate positions
of fish (and other aquatic animals) tagged with acoustic transmitters.
Based on registrations of acoustic transmitters on hydrophones positioned
in a fixed array, 'yaps' enables users to synchronize the collected data
(i.e. correcting for drift in the internal clocks of the
hydrophones/receivers) and subsequently to estimate tracks of the tagged
animals. The paper introducing 'yaps' is available in open access at
Baktoft, Gjelland, Økland & Thygesen (2017)
<doi:10.1038/s41598-017-14278-z>. Also check out our cookbook with a
completely worked through example at Baktoft, Gjelland, Økland, Rehage,
Rodemann, Corujo, Viadero & Thygesen (2019)
<DOI:10.1101/2019.12.16.877688>. Additional tutorials will eventually make
their way onto the project website at <https://baktoft.github.io/yaps/>.

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
