%global packname  sarsop
%global packver   0.6.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.4
Release:          1%{?dist}
Summary:          Approximate POMDP Planning Software

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-xml2 
Requires:         R-parallel 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-digest 
Requires:         R-Matrix 

%description
A toolkit for Partially Observed Markov Decision Processes (POMDP).
Provides bindings to C++ libraries implementing the algorithm SARSOP
(Successive Approximations of the Reachable Space under Optimal Policies)
and described in Kurniawati et al (2008), <doi:10.15607/RSS.2008.IV.009>.
This package also provides a high-level interface for generating, solving
and simulating POMDP problems and their solutions.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
