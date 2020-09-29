%global packname  nonmem2R
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Loading NONMEM Output Files with Functions for Visual Predictive Checks (VPC) and Goodness of Fit (GOF) Plots

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-MASS 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-reshape2 

%description
Loading NONMEM (NONlinear Mixed-Effect Modeling,
<http://www.iconplc.com/innovation/nonmem/>) and PSN (Perl-speaks-NONMEM,
<https://uupharmacometrics.github.io/PsN/>) output files to extract
parameter estimates, provide visual predictive check (VPC) and goodness of
fit (GOF) plots, and simulate with parameter uncertainty.

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
