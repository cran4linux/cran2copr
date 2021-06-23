%global __brp_check_rpaths %{nil}
%global packname  BayLum
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Chronological Bayesian Models Integrating Optically Stimulated Luminescence and Radiocarbon Age Dating

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.10
BuildRequires:    R-CRAN-runjags >= 2.0.4
BuildRequires:    R-CRAN-ArchaeoPhases >= 1.5
BuildRequires:    R-CRAN-Luminescence >= 0.8.2
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-CRAN-KernSmooth 
Requires:         R-CRAN-rjags >= 4.10
Requires:         R-CRAN-runjags >= 2.0.4
Requires:         R-CRAN-ArchaeoPhases >= 1.5
Requires:         R-CRAN-Luminescence >= 0.8.2
Requires:         R-utils 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-hexbin 
Requires:         R-CRAN-KernSmooth 

%description
Bayesian analysis of luminescence data and C-14 age estimates. Bayesian
models are based on the following publications: Combes, B. & Philippe, A.
(2017) <doi:10.1016/j.quageo.2017.02.003> and Combes et al (2015)
<doi:10.1016/j.quageo.2015.04.001>. This includes, amongst others, data
import, export, application of age models and palaeodose model.

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
