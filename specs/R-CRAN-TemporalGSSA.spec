%global __brp_check_rpaths %{nil}
%global packname  TemporalGSSA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Outputs Temporal Profile of Molecules Undergoing Stochastic Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The data that is generated from consecutive 'GillespieSSA' runs for a
generic biochemical network is formatted as "rows". The first column of
each row constitutes the computed timestep. Subsequent columns are used
for the participating molecules of a generic biochemical network. In this
way 'TemporalGSSA', may be considered a wrapper for the R-package
'GillespieSSA'. The number of observations must be at least 30. This will
generate data that is statistically significant. The user must also enter
an integer from 1-4. These specify the statistical modality utilized to
compute a representative timestep (mean, median, random, all). These
arguments are mandatory and will be checked. Whilst, the numeric indicator
"0" indicates suitability, "1" prompts the user to revise and re-enter
their data. An optional logical argument controls the output to the
console with the default being "TRUE" (curtailed) whilst "FALSE"
(verbose). The temporal profile of a molecule is necessary to comprehend
its' behaviour within the cell. This is accomplished by selecting a
representative timestep for a set of observations or consecutive runs (n
>= 30). A linear model of the numbers of each molecule is created with the
associated timestep from these observations. The coefficients of this
model (slope, constant) are then incorporated into a second linear
regression model. Here, the independent variable is the representative
timestep chosen previously. The generated data is the imputed molecule
number for an in silico experiment with (n >=30) observations. These steps
can be replicated with multiple set of observations or runs. The generated
"technical replicates" can be averaged and will constitute the
time-dependent data point of each molecule for a particular simulation
time. For varying simulation times these data will generate time-dependent
trajectories for each molecule of the biochemical network under study. The
algorithm has been deployed effectively in previous publications Kundu, S
(2021, Heliyon) <doi:10.1016/j.heliyon.2021.e07466> and (2016, Journal of
Theoretical Biology) <doi:10.1016/j.jtbi.2016.07.002>.

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
