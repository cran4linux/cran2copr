%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayLum
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Chronological Bayesian Models Integrating Optically Stimulated Luminescence and Radiocarbon Age Dating

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.13
BuildRequires:    R-CRAN-KernSmooth >= 2.23
BuildRequires:    R-CRAN-runjags >= 2.2.1
BuildRequires:    R-CRAN-ArchaeoPhases >= 1.8
BuildRequires:    R-CRAN-hexbin >= 1.28.3
BuildRequires:    R-CRAN-Luminescence >= 0.9.21
BuildRequires:    R-CRAN-coda >= 0.19
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-rjags >= 4.13
Requires:         R-CRAN-KernSmooth >= 2.23
Requires:         R-CRAN-runjags >= 2.2.1
Requires:         R-CRAN-ArchaeoPhases >= 1.8
Requires:         R-CRAN-hexbin >= 1.28.3
Requires:         R-CRAN-Luminescence >= 0.9.21
Requires:         R-CRAN-coda >= 0.19
Requires:         R-utils 
Requires:         R-methods 

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
