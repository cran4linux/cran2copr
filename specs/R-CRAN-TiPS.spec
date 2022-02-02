%global __brp_check_rpaths %{nil}
%global packname  TiPS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Trajectories and Phylogenies Simulator

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-inline 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-inline 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-utils 

%description
Generates stochastic time series and genealogies associated with a
population dynamics model. Times series are simulated using the Gillespie
exact and approximate algorithms and a new algorithm we introduce that
uses both approaches to optimize the time execution of the simulations.
Genealogies are simulated from a trajectory using a backwards-in-time
based approach. Methods are described in Danesh G et al (2020)
<doi:10.1101/2020.11.09.373795>.

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
