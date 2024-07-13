%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bamdit
%global packver   3.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Analysis of Diagnostic Test Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.0
BuildRequires:    R-CRAN-R2jags >= 0.04.03
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-rjags >= 4.0
Requires:         R-CRAN-R2jags >= 0.04.03
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-MASS 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 

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
