%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pref
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Preference Voting with Explanatory Graphics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-utils 
Requires:         R-base 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-jpeg 
Requires:         R-utils 

%description
Implements the Single Transferable Vote (STV) electoral system, with clear
explanatory graphics. The core function stv() uses Meek's method, the
purest expression of the simple principles of STV, but which requires
electronic counting. It can handle votes expressing equal preferences for
subsets of the candidates. A function stv.wig() implementing the Weighted
Inclusive Gregory method, as used in Scottish council elections, is also
provided, and with the same options, as described in the manual. The
required vote data format is as an R list: a function pref.data() is
provided to transform some commonly used data formats into this format.
References for methodology: Hill, Wichmann and Woodall (1987)
<doi:10.1093/comjnl/30.3.277>, Hill, David (2006)
<https://www.votingmatters.org.uk/ISSUE22/I22P2.pdf>, Mollison, Denis
(2023) <arXiv:2303.15310>, (see also the package manual
pref_pkg_manual.pdf).

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
