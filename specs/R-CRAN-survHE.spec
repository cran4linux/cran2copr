%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survHE
%global packver   2.0.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.51
Release:          1%{?dist}%{?buildtag}
Summary:          Survival Analysis in Health Economic Evaluation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-xlsx 
Requires:         R-tools 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Contains a suite of functions for survival analysis in health economics.
These can be used to run survival models under a frequentist (based on
maximum likelihood) or a Bayesian approach (both based on Integrated
Nested Laplace Approximation or Hamiltonian Monte Carlo). To run the
Bayesian models, the user needs to install additional modules (packages),
i.e. 'survHEinla' and 'survHEhmc'. These can be installed from
<https://giabaio.r-universe.dev/> using 'install.packages("survHEhmc",
repos = c("https://giabaio.r-universe.dev",
"https://cloud.r-project.org"))' and 'install.packages("survHEinla", repos
= c("https://giabaio.r-universe.dev", "https://cloud.r-project.org"))'
respectively. 'survHEinla' is based on the package INLA, which is
available for download at <https://inla.r-inla-download.org/R/stable/>.
The user can specify a set of parametric models using a common notation
and select the preferred mode of inference. The results can also be
post-processed to produce probabilistic sensitivity analysis and can be
used to export the output to an Excel file (e.g. for a Markov model, as
often done by modellers and practitioners). <doi:10.18637/jss.v095.i14>.

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
