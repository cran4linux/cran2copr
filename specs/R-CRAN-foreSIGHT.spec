%global packname  foreSIGHT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Systems Insights from Generation of Hydroclimatic Timeseries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-GA >= 3.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-rcorpora 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-GA >= 3.0
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-cowplot 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-rcorpora 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 

%description
A tool to create hydroclimate scenarios, stress test systems and visualize
system performance in scenario-neutral climate change impact assessments.
Scenario-neutral approaches 'stress-test' the performance of a modelled
system by applying a wide range of plausible hydroclimate conditions (see
Brown & Wilby (2012) <doi:10.1029/2012EO410001> and Prudhomme et al.
(2010) <doi:10.1016/j.jhydrol.2010.06.043>). These approaches allow the
identification of hydroclimatic variables that affect the vulnerability of
a system to hydroclimate variation and change. This tool enables the
generation of perturbed time series using a range of approaches including
simple scaling of observed time series (e.g. Culley et al. (2016)
<doi:10.1002/2015WR018253>) and stochastic simulation of perturbed time
series via an inverse approach (see Guo et al. (2018)
<doi:10.1016/j.jhydrol.2016.03.025>). It incorporates 'Richardson-type'
weather generator model configurations documented in Richardson (1981)
<doi:10.1029/WR017i001p00182>, Richardson and Wright (1984), as well as
latent variable type model configurations documented in Bennett et al.
(2018) <doi:10.1016/j.jhydrol.2016.12.043>, Rasmussen (2013)
<doi:10.1002/wrcr.20164>, Bennett et al. (2019)
<doi:10.5194/hess-23-4783-2019> to generate hydroclimate variables on a
daily basis (e.g. precipitation, temperature, potential
evapotranspiration) and allows a variety of different hydroclimate
variable properties, herein called attributes, to be perturbed. Options
are included for the easy integration of existing system models both
internally in R and externally for seamless 'stress-testing'. A suite of
visualization options for the results of a scenario-neutral analysis (e.g.
plotting performance spaces and overlaying climate projection information)
are also included. As further developments in scenario-neutral approaches
occur the tool will be updated to incorporate these advances.

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
