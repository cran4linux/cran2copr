%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SAME
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Seamless Adaptive Multi-Arm Multi-Stage Enrichment

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-expint 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-expint 

%description
Design a Bayesian seamless multi-arm biomarker-enriched phase II/III
design with the survival endpoint with allowing sample size re-estimation.
James M S Wason, Jean E Abraham, Richard D Baird, Ioannis Gournaris,
Anne-Laure Vallier, James D Brenton, Helena M Earl, Adrian P Mander (2015)
<doi:10.1038/bjc.2015.278>. Guosheng Yin, Nan Chen, J. Jack Lee (2018)
<doi:10.1007/s12561-017-9199-7>. Ying Yuan, Beibei Guo, Mark Munsell,
Karen Lu, Amir Jazaeri (2016) <doi:10.1002/sim.6971>.

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
