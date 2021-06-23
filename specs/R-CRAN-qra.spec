%global __brp_check_rpaths %{nil}
%global packname  qra
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Quantal Response Analysis for Dose-Mortality Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-splines 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lme4 
Requires:         R-splines 

%description
Functions are provided that implement the use of the Fieller's formula
methodology, for calculating a confidence interval for a ratio of
(possibly, correlated) means.  See Fieller (1954)
<doi:10.1111/j.2517-6161.1954.tb00159.x>.  Here, the application of
primary interest is to studies of insect mortality response to increasing
doses of a fumigant, or, e.g., to time in coolstorage. The formula is used
to calculate a confidence interval for the dose or time required to
achieve a specified mortality proportion, commonly 0.5 or 0.99.  A
vignette demonstrates link functions that may be considered, and
alternative choices of error family.  Note in particular the beta-binomial
error family.  See also Maindonald, Waddell, and Petry (2001)
<doi:10.1016/S0925-5214(01)00082-5>.

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
