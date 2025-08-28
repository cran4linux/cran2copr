%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SampleSizeCalculator
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sample Size Calculator under Complex Survey Design

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinythemes 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-bslib 
Requires:         R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinythemes 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-bslib 

%description
It helps in determination of sample size for estimating population mean or
proportion under simple random sampling with or without replacement and
stratified random sampling without replacement. When prior information on
the population coefficient of variation (CV) is unavailable, then a
preliminary sample is drawn to estimate the CV which is used to compute
the final sample size. If the final size exceeds the preliminary sample
size, then additional units are drawn; otherwise, the preliminary sample
size is considered as final sample size. For stratified random sampling
without replacement design, it also calculates the sample size in each
stratum under different allocation methods for estimation of population
mean and proportion based upon the availability of prior information on
sizes of the strata, standard deviations of the strata and costs of
drawing a sampling unit in the strata.For details on sampling methodology,
see, Cochran (1977) "Sampling Techniques"
<https://archive.org/details/samplingtechniqu0000coch_t4x6>.

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
