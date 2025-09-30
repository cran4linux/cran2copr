%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BOP2FE
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Optimal Phase II Design with Futility and Efficacy Stopping Boundaries

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-utils 

%description
Bayesian optimal design with futility and efficacy stopping boundaries
(BOP2-FE) is a novel statistical framework for single-arm Phase II
clinical trials. It enables early termination for efficacy when interim
data are promising, while explicitly controlling Type I and Type II error
rates. The design supports a variety of endpoint structures, including
single binary endpoints, nested endpoints, co-primary endpoints, and joint
monitoring of efficacy and toxicity. The package provides tools for
enumerating stopping boundaries prior to trial initiation and for
conducting simulation studies to evaluate the design’s operating
characteristics. Users can flexibly specify design parameters to suit
their specific applications. For methodological details, refer to Xu et
al. (2025) <doi:10.1080/10543406.2025.2558142>.

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
