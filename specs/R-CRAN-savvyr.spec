%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  savvyr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis for AdVerse Events with VarYing Follow-Up Times

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-etm 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-etm 
Requires:         R-CRAN-Rdpack 

%description
The SAVVY (Survival Analysis for AdVerse Events with VarYing Follow-Up
Times) project is a consortium of academic and pharmaceutical industry
partners that aims to improve the analyses of adverse event (AE) data in
clinical trials through the use of survival techniques appropriately
dealing with varying follow-up times and competing events, see Stegherr,
Schmoor, Beyersmann, et al. (2021) <doi:10.1186/s13063-021-05354-x>.
Although statistical methodologies have advanced, in AE analyses often the
incidence proportion, the incidence density or a non-parametric
Kaplan-Meier estimator are used, which either ignore censoring or
competing events. This package contains functions to easily conduct the
proposed improved AE analyses.

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
