%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cbcTools
%global packver   0.6.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.3
Release:          1%{?dist}%{?buildtag}
Summary:          Design and Analyze Choice-Based Conjoint Experiments

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-idefix >= 1.1.0
BuildRequires:    R-CRAN-logitr >= 1.0.1
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-idefix >= 1.1.0
Requires:         R-CRAN-logitr >= 1.0.1
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-rlang 
Requires:         R-tools 
Requires:         R-stats 
Requires:         R-utils 

%description
Design and evaluate choice-based conjoint survey experiments. Generate a
variety of survey designs, including random designs, frequency-based
designs, and D-optimal designs, as well as "labeled" designs (also known
as "alternative-specific designs"), designs with "no choice" options, and
designs with dominant alternatives removed. Conveniently inspect and
compare designs using a variety of metrics, including design balance,
overlap, and D-error, and simulate choice data for a survey design either
randomly or according to a utility model defined by user-provided prior
parameters. Conduct a power analysis for a given survey design by
estimating the same model on different subsets of the data to simulate
different sample sizes. Bayesian D-efficient designs using the 'cea' and
'modfed' methods are obtained using the 'idefix' package by Traets et al
(2020) <doi:10.18637/jss.v096.i03>. Choice simulation and model estimation
in power analyses are handled using the 'logitr' package by Helveston
(2023) <doi:10.18637/jss.v105.i10>.

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
