%global packname  GPGame
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Solving Complex Game Problems using Gaussian Processes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-GPareto 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-DiceDesign 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-GPareto 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-DiceDesign 
Requires:         R-MASS 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 

%description
Sequential strategies for finding a game equilibrium are proposed in a
black-box setting (expensive pay-off evaluations, no derivatives). The
algorithm handles noiseless or noisy evaluations. Two acquisition
functions are available. Graphical outputs can be generated automatically.

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
