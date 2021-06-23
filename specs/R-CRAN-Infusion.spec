%global __brp_check_rpaths %{nil}
%global packname  Infusion
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Inference Using Simulation

License:          CeCILL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spaMM >= 3.6.0
BuildRequires:    R-CRAN-blackbox >= 1.0.14
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-spaMM >= 3.6.0
Requires:         R-CRAN-blackbox >= 1.0.14
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-mvtnorm 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-foreach 

%description
Implements functions for simulation-based inference. In particular,
implements functions to perform likelihood inference from data summaries
whose distributions are simulated (Rousset et al. 2017
<doi:10.1111/1755-0998.12627>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
