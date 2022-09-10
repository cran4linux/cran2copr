%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binfunest
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimates Parameters of Functions Driving Binomial Random Variables

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-stats4 

%description
Provides maximum likelihood estimates of the performance parameters that
drive a binomial distribution of observed errors, and takes full advantage
of zero error observations. High performance communications systems
typically have inherent noise sources and other performance limitations
that need to be estimated. Measurements made at high signal to noise
ratios typically result in zero errors due to limitation in available
measurement time. Package includes theoretical performance functions for
common modulation schemes (Proakis, "Digital Communications" (1995,
<ISBN:0-07-051726-6>)), polarization shifted QPSK (Agrell & Karlsson
(2009, <DOI:10.1109/JLT.2009.2029064>)), and utility functions to work
with the performance functions.

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
