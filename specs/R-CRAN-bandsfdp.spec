%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bandsfdp
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Compute Upper Prediction Bounds on the FDP in Competition-Based Setups

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements functions that calculate upper prediction bounds on the false
discovery proportion (FDP) in the list of discoveries returned by
competition-based setups, implementing Ebadi et al. (2022)
<arXiv:2302.11837>. Such setups include target-decoy competition (TDC) in
computational mass spectrometry and the knockoff construction in linear
regression (note this package typically uses the terminology of TDC).
Included is the standardized (TDC-SB) and uniform (TDC-UB) bound on TDC's
FDP, and the simultaneous standardized and uniform bands. Requires
pre-computed Monte Carlo statistics available at
<https://github.com/uni-Arya/fdpbandsdata>. This data can be downloaded by
running the command 'devtools::install_github("uni-Arya/fdpbandsdata")' in
R and restarting R after installation. The size of this data is roughly
81Mb.

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
