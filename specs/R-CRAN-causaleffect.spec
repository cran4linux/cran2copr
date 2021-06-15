%global packname  causaleffect
%global packver   1.3.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.13
Release:          1%{?dist}%{?buildtag}
Summary:          Deriving Expressions of Joint Interventional Distributions and Transport Formulas in Causal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-igraph 

%description
Functions for identification and transportation of causal effects.
Provides a conditional causal effect identification algorithm (IDC) by
Shpitser, I. and Pearl, J. (2006)
<http://ftp.cs.ucla.edu/pub/stat_ser/r329-uai.pdf>, an algorithm for
transportability from multiple domains with limited experiments by
Bareinboim, E. and Pearl, J. (2014)
<http://ftp.cs.ucla.edu/pub/stat_ser/r443.pdf> and a selection bias
recovery algorithm by Bareinboim, E. and Tian, J. (2015)
<http://ftp.cs.ucla.edu/pub/stat_ser/r445.pdf>. All of the previously
mentioned algorithms are based on a causal effect identification algorithm
by Tian , J. (2002) <http://ftp.cs.ucla.edu/pub/stat_ser/r309.pdf>.

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
