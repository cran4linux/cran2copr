%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssifs
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Stochastic Search Inconsistency Factor Selection

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-meta >= 8.0.1
BuildRequires:    R-utils >= 4.2.0
BuildRequires:    R-CRAN-gtools >= 3.9.2.1
BuildRequires:    R-CRAN-ggplot2 >= 3.3.6
BuildRequires:    R-CRAN-netmeta >= 3.0.2
BuildRequires:    R-CRAN-Rdpack >= 2.3
BuildRequires:    R-CRAN-plyr >= 1.8.7
BuildRequires:    R-CRAN-igraph >= 1.3.1
BuildRequires:    R-CRAN-R2jags >= 0.7.1
Requires:         R-CRAN-meta >= 8.0.1
Requires:         R-utils >= 4.2.0
Requires:         R-CRAN-gtools >= 3.9.2.1
Requires:         R-CRAN-ggplot2 >= 3.3.6
Requires:         R-CRAN-netmeta >= 3.0.2
Requires:         R-CRAN-Rdpack >= 2.3
Requires:         R-CRAN-plyr >= 1.8.7
Requires:         R-CRAN-igraph >= 1.3.1
Requires:         R-CRAN-R2jags >= 0.7.1

%description
Evaluating the consistency assumption of Network Meta-Analysis both
globally and locally in the Bayesian framework. Inconsistencies are
located by applying Bayesian variable selection to the inconsistency
factors. The implementation of the method is described by Seitidis et al.
(2023) <doi:10.1002/sim.9891>.

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
