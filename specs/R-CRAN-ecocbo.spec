%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecocbo
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          Calculating Optimum Sampling Effort in Community Ecology

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-sampling 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-parabar 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-SSP 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-sampling 
Requires:         R-stats 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-parabar 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-SSP 
Requires:         R-CRAN-plotly 

%description
A system for calculating the optimal sampling effort, based on the ideas
of "Ecological cost-benefit optimization" as developed by A. Underwood
(1997, ISBN 0 521 55696 1). Data is obtained from simulated ecological
communities with prep_data() which formats and arranges the initial data,
and then the optimization follows the following procedure of four
functions: (1) prep_data() takes the original dataset and creates
simulated sets that can be used as a basis for estimating statistical
power and type II error. (2) sim_beta() is used to estimate the
statistical power for the different sampling efforts specified by the
user. (3) sim_cbo() calculates then the optimal sampling effort, based on
the statistical power and the sampling costs. Additionally, (4) scompvar()
calculates the variation components necessary for (5) Underwood_cbo() to
calculate the optimal combination of number of sites and samples depending
on either an economic budget or on a desired statistical accuracy. Lastly,
(6) plot_power() helps the user visualize the results of sim_beta().

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
