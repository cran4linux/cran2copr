%global __brp_check_rpaths %{nil}
%global packname  etrm
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Energy Trading and Risk Management

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-methods 

%description
Provides a collection of functions to perform core tasks within Energy
Trading and Risk Management (ETRM). Calculation of maximum smoothness
forward price curves for electricity and natural gas contracts with flow
delivery, as presented in F. E. Benth, S. Koekebakker, and F. Ollmar
(2007) <doi:10.3905/jod.2007.694791> and F. E. Benth, J. S. Benth, and S.
Koekebakker (2008) <doi:10.1142/6811>. Portfolio insurance trading
strategies for price risk management in the forward market, see F. Black
(1976) <doi:10.1016/0304-405X(76)90024-6>, T. Bjork (2009)
<https://EconPapers.repec.org/RePEc:oxp:obooks:9780199574742>, F. Black
and R. W. Jones (1987) <doi:10.3905/jpm.1987.409131> and H. E. Leland
(1980) <http://www.jstor.org/stable/2327419>.

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
