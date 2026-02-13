%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  drimmR
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation, Simulation and Reliability of Drifting Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-reshape2 

%description
Performs the drifting Markov models (DMM) which are non-homogeneous Markov
models designed for modeling the heterogeneities of sequences in a more
flexible way than homogeneous Markov chains or even hidden Markov models.
In this context, we developed an R package dedicated to the estimation,
simulation and the exact computation of associated reliability of drifting
Markov models. The implemented methods are described in Vergne, N. (2008),
<doi:10.2202/1544-6115.1326> and Barbu, V.S., Vergne, N. (2019)
<doi:10.1007/s11009-018-9682-8> .

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
