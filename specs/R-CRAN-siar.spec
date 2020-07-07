%global packname  siar
%global packver   4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.2
Release:          2%{?dist}
Summary:          Stable Isotope Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-bayesm 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-CRAN-hdrcde 
Requires:         R-CRAN-coda 
Requires:         R-MASS 
Requires:         R-CRAN-bayesm 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-spatstat 

%description
This package takes data on organism isotopes and fits a Bayesian model to
their dietary habits based upon a Gaussian likelihood with a mixture
dirichlet-distributed prior on the mean. It also includes SiBER metrics.
See siardemo() for an example. Version 4.1.2 contains bug fixes to allow
more than isotope numbers other than 2. Version 4.2 fixes a bug that
stopped siar working on 64-bit systems

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
