%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sim.BA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simulation-Based Bias Analysis for Observational Studies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cobalt >= 4.5.3
BuildRequires:    R-CRAN-ggplot2 >= 3.4.4
BuildRequires:    R-CRAN-pbapply >= 1.7.2
BuildRequires:    R-CRAN-scales >= 1.3.0
BuildRequires:    R-CRAN-rlang >= 1.1.3
BuildRequires:    R-CRAN-chk >= 0.9.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-utils 
Requires:         R-CRAN-cobalt >= 4.5.3
Requires:         R-CRAN-ggplot2 >= 3.4.4
Requires:         R-CRAN-pbapply >= 1.7.2
Requires:         R-CRAN-scales >= 1.3.0
Requires:         R-CRAN-rlang >= 1.1.3
Requires:         R-CRAN-chk >= 0.9.1
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-utils 

%description
Allows user to conduct a simulation based quantitative bias analysis using
covariate structures generated with individual-level data to characterize
the bias arising from unmeasured confounding. Users can specify their
desired data generating mechanisms to simulate data and quantitatively
summarize findings in an end-to-end application using this package.

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
