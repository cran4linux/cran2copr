%global packname  meboot
%global packver   1.4-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.9
Release:          1%{?dist}%{?buildtag}
Summary:          Maximum Entropy Bootstrap for Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-dynlm 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-tdigest 
BuildRequires:    R-CRAN-hdrcde 
Requires:         R-CRAN-dynlm 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-tdigest 
Requires:         R-CRAN-hdrcde 

%description
Maximum entropy density based dependent data bootstrap. An algorithm is
provided to create a population of time series (ensemble) without assuming
stationarity. The reference paper (Vinod, H.D., 2004 <DOI:
10.1016/j.jempfin.2003.06.002>) explains how the algorithm satisfies the
ergodic theorem and the central limit theorem.

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
