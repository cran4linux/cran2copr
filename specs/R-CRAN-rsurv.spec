%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rsurv
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Random Generation of Survival Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bellreg >= 0.0.2.2
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-stabledist 
Requires:         R-CRAN-bellreg >= 0.0.2.2
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-stabledist 

%description
Random generation of survival data from a wide range of regression models,
including accelerated failure time (AFT), proportional hazards (PH),
proportional odds (PO), accelerated hazard (AH), Yang and Prentice (YP),
and extended hazard (EH) models. The package 'rsurv' also stands out by
its ability to generate survival data from an unlimited number of baseline
distributions provided that an implementation of the quantile function of
the chosen baseline distribution is available in R. Another nice feature
of the package 'rsurv' lies in the fact that linear predictors are
specified via a formula-based approach, facilitating the inclusion of
categorical variables and interaction terms. The functions implemented in
the package 'rsurv' can also be employed to simulate survival data with
more complex structures, such as survival data with different types of
censoring mechanisms, survival data with cure fraction, survival data with
random effects (frailties), multivariate survival data, and competing
risks survival data. Details about the R package 'rsurv' can be found in
Demarqui (2024) <doi:10.48550/arXiv.2406.01750>.

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
