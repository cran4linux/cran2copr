%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TemporalGSSA
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Outputs Temporal Profile of Molecules from Stochastic Simulation Algorithm Generated Datasets

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The data that is generated from independent and consecutive 'GillespieSSA'
runs for a generic biochemical network is formatted as rows and
constitutes an observation. The first column of each row is the computed
timestep for each run. Subsequent columns are used for the number of
molecules of each participating molecular species or "metabolite" of a
generic biochemical network. In this way 'TemporalGSSA', is a wrapper for
the R-package 'GillespieSSA'. The number of observations must be at least
30. This will generate data that is statistically significant.
'TemporalGSSA', transforms this raw data into a simulation time-dependent
and metabolite-specific trial. Each such trial is defined as a set of
linear models (n >= 30) between a timestep and number of molecules for a
metabolite. Each linear model is characterized by coefficients such as the
slope, arbitrary constant, etc. The user must enter an integer from 1-4.
These specify the statistical modality utilized to compute a
representative timestep (mean, median, random, all). These arguments are
mandatory and will be checked. Whilst, the numeric indicator "0" indicates
suitability, "1" prompts the user to revise and re-enter their data. An
optional logical argument controls the output to the console with the
default being "TRUE" (curtailed) whilst "FALSE" (verbose). The
coefficients of each linear model are averaged (mean slope, mean constant)
and are incorporated into a metabolite-specific linear regression model as
the dependent variable. The independent variable is the representative
timestep chosen previously. The generated data is the imputed molecule
number for an in silico experiment with (n >=30) observations. These steps
can be replicated with multiple set of observations. The generated
"technical replicates" can be statistically evaluated (mean, standard
deviation) and will constitute simulation time-dependent molecules for
each metabolite. For SSA-generated datasets with varying simulation times
'TemporalGSSA' will generate a simulation time-dependent trajectory for
each metabolite of the biochemical network under study. The relevant
publication with the mathematical derivation of the algorithm is (2022,
Journal of Bioinformatics and Computational Biology)
<doi:10.1142/S0219720022500184>. The algorithm has been deployed in the
following publications (2021, Heliyon) <doi:10.1016/j.heliyon.2021.e07466>
and (2016, Journal of Theoretical Biology)
<doi:10.1016/j.jtbi.2016.07.002>.

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
