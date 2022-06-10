%global __brp_check_rpaths %{nil}
%global packname  iccCounts
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Intraclass Correlation Coefficient for Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmmTMB 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Deriv 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-glmmTMB 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Deriv 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-dplyr 

%description
Estimates the intraclass correlation coefficient (ICC) for count data to
assess repeatability (intra-methods concordance) and concordance
(between-method concordance). In the concordance setting, the ICC is
equivalent to the concordance correlation coefficient estimated by
variance components. The ICC is estimated using the estimates from
generalized linear mixed models. The within-subjects distributions
considered are: Poisson; Negative Binomial with additive and proportional
extradispersion; Zero-Inflated Poisson; and Zero-Inflated Negative
Binomial with additive and proportional extradispersion. The statistical
methodology used to estimate the ICC with count data can be found in
Carrasco (2010) <doi:10.1111/j.1541-0420.2009.01335.x>.

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
