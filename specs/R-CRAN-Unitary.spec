%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Unitary
%global packver   0.3.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.11
Release:          1%{?dist}%{?buildtag}
Summary:          Quantum Simulator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-Formula 
Requires:         R-grid 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-data.table 

%description
Provides a comprehensive toolkit for quantum computing simulation and
visualization within the R environment. The package enables users to
initialize qubit states, construct custom quantum gates with both unitary
transformation and visual parameters, and build full quantum circuits by
sequentially adding gates. It includes predefined common gates (e.g.,
Hadamard, Pauli-X/Y/Z, Control-NOT, Control-Z) and supports direct
plotting of circuits and individual gates for intuitive analysis.

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
