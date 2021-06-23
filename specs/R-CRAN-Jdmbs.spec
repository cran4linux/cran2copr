%global __brp_check_rpaths %{nil}
%global packname  Jdmbs
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Monte Carlo Option Pricing Algorithms for Jump Diffusion Modelswith Correlational Companies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-png 
Requires:         R-CRAN-ggplot2 

%description
Option is a one of the financial derivatives and its pricing is an
important problem in practice. The process of stock prices are represented
as Geometric Brownian motion [Black (1973) <doi:10.1086/260062>] or jump
diffusion processes [Kou (2002) <doi:10.1287/mnsc.48.8.1086.166>]. In this
package, algorithms and visualizations are implemented by Monte Carlo
method in order to calculate European option price for three equations by
Geometric Brownian motion and jump diffusion processes and furthermore a
model that presents jumps among companies affect each other.

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
