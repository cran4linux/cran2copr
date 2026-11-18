%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survivalGPU
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fast and Scalable Implementations for Survival Models

License:          LGPL (>= 2.1)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-reticulate 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Performs survival analysis on graphics processing units (GPUs) using Cox
proportional hazards and weighted cumulative exposure (WCE) models, with
support for bootstrap resampling and memory management. The Cox model is
described in Cox (1972) <doi:10.1111/j.2517-6161.1972.tb00899.x> and the
WCE model in Sylvestre and Abrahamowicz (2009) <doi:10.1002/sim.3701>.
Computations are delegated to 'PyTorch' via 'reticulate'; the WCE model
additionally requires 'PyKeOps', which is not available natively on
Windows, but can be used there through the Windows Subsystem for Linux
('WSL').

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
