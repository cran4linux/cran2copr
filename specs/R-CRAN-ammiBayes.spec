%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ammiBayes
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Ammi Model for Continuous Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-distfree.cr 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-bayesplot 
BuildRequires:    R-CRAN-Hmisc 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-distfree.cr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-bayesplot 
Requires:         R-CRAN-Hmisc 

%description
Flexible multi-environment trials analysis via MCMC method for Additive
Main Effects and Multiplicative Model (AMMI) for continuous data. Biplot
with the averages and regions of confidence can be generated. The chains
run in parallel on Linux systems and run serially on Windows.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
