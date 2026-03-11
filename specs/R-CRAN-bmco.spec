%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bmco
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis for Multivariate Categorical Outcomes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-MCMCpack 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-pgdraw 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-MCMCpack 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-pgdraw 
Requires:         R-tcltk 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Provides Bayesian methods for comparing groups on multiple binary
outcomes. Includes basic tests using multivariate Bernoulli distributions,
subgroup analysis via generalized linear models, and multilevel models for
clustered data. For statistical underpinnings, see Kavelaars, Mulder, and
Kaptein (2020) <doi:10.1177/0962280220922256>, Kavelaars, Mulder, and
Kaptein (2024) <doi:10.1080/00273171.2024.2337340>, and Kavelaars, Mulder,
and Kaptein (2023) <doi:10.1186/s12874-023-02034-z>. An interactive shiny
app to perform sample size computations is available.

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
