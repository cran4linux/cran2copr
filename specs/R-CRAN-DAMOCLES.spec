%global packname  DAMOCLES
%global packver   2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Dynamic Assembly Model of Colonization, Local Extinction andSpeciation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DDD >= 3.0
BuildRequires:    R-CRAN-caper 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-picante 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-DAISIE 
Requires:         R-CRAN-DDD >= 3.0
Requires:         R-CRAN-caper 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-picante 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-DAISIE 

%description
Simulates and computes (maximum) likelihood of a dynamical model of
community assembly that takes into account phylogenetic history.

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
