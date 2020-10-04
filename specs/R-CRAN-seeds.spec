%global packname  seeds
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate Hidden Inputs using the Dynamic Elastic Net

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Deriv >= 3.8
BuildRequires:    R-CRAN-pracma >= 2.1.4
BuildRequires:    R-CRAN-deSolve >= 1.20
BuildRequires:    R-CRAN-Ryacas 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-callr 
Requires:         R-CRAN-Deriv >= 3.8
Requires:         R-CRAN-pracma >= 2.1.4
Requires:         R-CRAN-deSolve >= 1.20
Requires:         R-CRAN-Ryacas 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-callr 

%description
Algorithms to calculate the hidden inputs of systems of differential
equations. These hidden inputs can be interpreted as a control that tries
to minimize the discrepancies between a given model and taken
measurements. The idea is also called the Dynamic Elastic Net, as proposed
in the paper "Learning (from) the errors of a systems biology model"
(Engelhardt, Froelich, Kschischo 2016) <doi:10.1038/srep20772>. To use the
experimental SBML import function, the 'rsbml' package is required. For
installation I refer to the official 'rsbml' page:
<https://bioconductor.org/packages/release/bioc/html/rsbml.html>.

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
