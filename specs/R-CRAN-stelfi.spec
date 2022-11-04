%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stelfi
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Hawkes and Log-Gaussian Cox Point Processes Using Template Model Builder

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-TMB >= 1.7.20
BuildRequires:    R-CRAN-sf >= 1.0.8
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-TMB >= 1.7.20
Requires:         R-CRAN-sf >= 1.0.8
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-Matrix 

%description
Fit Hawkes and log-Gaussian Cox process models with extensions. Introduced
in Hawkes (1971) <doi:10.2307/2334319> a Hawkes process is a self-exciting
temporal point process where the occurrence of an event immediately
increases the chance of another. We extend this to consider
self-inhibiting process and a non-homogeneous background rate. A
log-Gaussian Cox process is a Poisson point process where the
log-intensity is given by a Gaussian random field. We extend this to a
joint likelihood formulation fitting a marked log-Gaussian Cox model. In
addition, the package offers functionality to fit self-exciting
spatiotemporal point processes. Models are fitted via maximum likelihood
using 'TMB' (Template Model Builder). Where included 1) random fields are
assumed to be Gaussian and are integrated over using the Laplace
approximation and 2) a stochastic partial differential equation model,
introduced by Lindgren, Rue, and Lindström. (2011)
<doi:10.1111/j.1467-9868.2011.00777.x>, is defined for the field(s).

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
