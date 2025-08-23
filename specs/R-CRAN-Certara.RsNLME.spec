%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Certara.RsNLME
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pharmacometric Modeling

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-Certara.NLME8 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ssh 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-Certara.NLME8 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-ssh 

%description
Facilitate Pharmacokinetic (PK) and Pharmacodynamic (PD) modeling and
simulation with powerful tools for Nonlinear Mixed-Effects (NLME)
modeling. The package provides access to the same advanced Maximum
Likelihood algorithms used by the NLME-Engine in the Phoenix platform.
These tools support a range of analyses, from parametric methods to
individual and pooled data, and support integrated use within the Pirana
pharmacometric workbench <doi:10.1002/psp4.70067>. Execution is supported
both locally or on remote machines.

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
