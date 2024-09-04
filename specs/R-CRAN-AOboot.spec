%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AOboot
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bootstrapping in Different One-Way and Two-Way ANOVA

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-afex 
BuildRequires:    R-CRAN-emmeans 
BuildRequires:    R-CRAN-lsr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-carData 
Requires:         R-CRAN-afex 
Requires:         R-CRAN-emmeans 
Requires:         R-CRAN-lsr 
Requires:         R-methods 
Requires:         R-CRAN-carData 

%description
To address the violation of the assumption of normally distributed
variables, researchers frequently employ bootstrapping. Building upon
established packages for R (Sigmann et al. (2024)
<doi:10.32614/CRAN.package.afex>, Lenth (2024)
<doi:10.32614/CRAN.package.emmeans>), we provide bootstrapping functions
to approximate a normal distribution of the parameter estimates for
between-subject, within-subject, and mixed one-way and two-way ANOVA.

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
