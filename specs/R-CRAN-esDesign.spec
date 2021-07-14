%global __brp_check_rpaths %{nil}
%global packname  esDesign
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Enrichment Designs with Sample Size Re-Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Software of 'esDesign' is developed to implement the adaptive enrichment
designs with sample size re-estimation presented in Lin et al. (2021)
<doi: 10.1016/j.cct.2020.106216>. In details, three-proposed trial designs
are provided, including the AED1-SSR (or ES1-SSR), AED2-SSR (or ES2-SSR)
and AED3-SSR (or ES3-SSR). In addition, this package also contains several
widely used adaptive designs, such as the Marker Sequential Test (MaST)
design proposed Freidlin et al. (2014) <doi:10.1177/1740774513503739>, the
adaptive enrichment designs without early stopping (AED or ES), the sample
size re-estimation procedure (SSR) based on the conditional power proposed
by Proschan and Hunsberger (1995), and some useful functions. In details,
we can calculate the futility and/or efficacy stopping boundaries, the
sample size required, calibrate the value of the threshold of the
difference between subgroup-specific test statistics, conduct the
simulation studies in AED, SSR, AED1-SSR, AED2-SSR and AED3-SSR.

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
