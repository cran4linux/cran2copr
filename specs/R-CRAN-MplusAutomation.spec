%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MplusAutomation
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          An R Package for Facilitating Large-Scale Latent Variable Analyses in Mplus

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-texreg 
BuildRequires:    R-CRAN-pander 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-texreg 
Requires:         R-CRAN-pander 
Requires:         R-CRAN-digest 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-checkmate 

%description
Leverages the R language to automate latent variable model estimation and
interpretation using 'Mplus', a powerful latent variable modeling program
developed by Muthen and Muthen (<https://www.statmodel.com>).
Specifically, this package provides routines for creating related groups
of models, running batches of models, and extracting and tabulating model
parameters and fit statistics.

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
