%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  clockSim
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Streamlined Simulation of Circadian Gene Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-bench 
BuildRequires:    R-CRAN-dde 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lomb 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-odin 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-bench 
Requires:         R-CRAN-dde 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lomb 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-odin 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
A user-friendly workflow for simulating circadian clock gene networks.
Despite decades of advances in modeling circadian clock dynamics, the lack
of accessible tools for reproducible simulation workflows hinders the
integration of computational modeling with experimental studies.
'clockSim' addresses this gap by providing models and helper functions
with step-by-step vignettes. This package opens up system-level
exploration of the circadian clock to wet-lab experimentalists, and future
development will include additional clock architectures and other gene
circuit models. Currently implemented models are based on Leloup and
Goldbeter (1998) <doi:10.1177/074873098128999934>.

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
