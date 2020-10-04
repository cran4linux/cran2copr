%global packname  mvMORPH
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          2%{?dist}%{?buildtag}
Summary:          Multivariate Comparative Tools for Fitting Evolutionary Modelsto Morphometric Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-glassoFast 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-subplex 
Requires:         R-stats 
Requires:         R-CRAN-spam 
Requires:         R-graphics 
Requires:         R-CRAN-glassoFast 
Requires:         R-parallel 
Requires:         R-CRAN-pbmcapply 

%description
Fits multivariate (Brownian Motion, Early Burst, ACDC, Ornstein-Uhlenbeck
and Shifts) models of continuous traits evolution on trees and time
series. 'mvMORPH' also proposes high-dimensional multivariate comparative
tools (linear models using Generalized Least Squares and multivariate
tests) based on penalized likelihood.  See Clavel et al. (2015)
<DOI:10.1111/2041-210X.12420>, Clavel et al. (2019)
<DOI:10.1093/sysbio/syy045>, and Clavel & Morlon (2020)
<DOI:10.1093/sysbio/syaa010>.

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

%files
%{rlibdir}/%{packname}
