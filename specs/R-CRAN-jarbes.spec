%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  jarbes
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Just a Rather Bayesian Evidence Synthesis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-mcmcplots 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-GGally 
BuildRequires:    R-CRAN-qpdf 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-R2jags 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-MASS 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-mcmcplots 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-GGally 
Requires:         R-CRAN-qpdf 

%description
Provides a new class of Bayesian meta-analysis models that incorporates a
model for internal and external validity bias. In this way, it is possible
to combine studies of diverse quality and different types. For example, we
can combine the results of randomized control trials (RCTs) with the
results of observational studies (OS).

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
