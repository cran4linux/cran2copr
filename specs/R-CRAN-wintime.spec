%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wintime
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Win Time Methods for Time-to-Event Data in Clinical Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-survival 

%description
Performs an analysis of time-to-event clinical trial data using various
"win time" methods, including 'ewt', 'ewtr', 'rmt', 'ewtp', 'rewtp',
'ewtpr', 'rewtpr', 'max', 'wtr', 'rwtr', 'pwt', and 'rpwt'. These methods
are used to calculate and compare treatment effects on ordered composite
endpoints. The package handles event times, event indicators, and
treatment arm indicators and supports calculations on observed and
resampled data. Detailed explanations of each method and usage examples
are provided in "Use of win time for ordered composite endpoints in
clinical trials," by Troendle et al.
(2024)<https://pubmed.ncbi.nlm.nih.gov/38417455/>. For more information,
see the package documentation or the vignette titled "Introduction to
wintime."

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
