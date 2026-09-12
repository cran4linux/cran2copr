%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.NLME8
%global packver   3.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Utilities for Certara's Nonlinear Mixed-Effects Modeling Engine

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-batchtools >= 0.9.9
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-batchtools >= 0.9.9
Requires:         R-CRAN-xml2 
Requires:         R-utils 
Requires:         R-CRAN-data.table 

%description
Interface to Certara's Nonlinear Mixed-Effects (NLME) modeling engine
('NLME-Engine') for pharmacokinetic and pharmacodynamic (PK/PD) modeling
and simulation. Provides access to the Maximum Likelihood estimation
algorithms available in the 'Phoenix' NLME platform for population,
individual, and pooled analyses using parametric methods. Includes
utilities for setting up NLME installations and parallel settings, running
estimation, bootstrap, and covariate search workflows, and updating model
files from engine output. Jobs can be executed locally or across
high-performance computing resources, including Linux Sun Grid Engine
(SGE) and Simple Linux Utility for Resource Management (SLURM) grids as
well as multicore Linux and Windows hosts.

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
