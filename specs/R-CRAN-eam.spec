%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eam
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evidence Accumulation Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-stats 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-distributional 
Requires:         R-stats 
Requires:         R-parallel 
Requires:         R-CRAN-codetools 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 

%description
Simulation-based evidence accumulation models for analyzing responses and
reaction times in single- and multi-response tasks. The package includes
simulation engines for five representative models: the Diffusion Decision
Model (DDM), Leaky Competing Accumulator (LCA), Linear Ballistic
Accumulator (LBA), Racing Diffusion Model (RDM), and Levy Flight Model
(LFM), and extends these frameworks to multi-response settings. The
package supports user-defined functions for item-level parameterization
and the incorporation of covariates, enabling flexible customization and
the development of new model variants based on existing architectures.
Inference is performed using simulation-based methods, including
Approximate Bayesian Computation (ABC) and Amortized Bayesian Inference
(ABI), which allow parameter estimation without requiring tractable
likelihood functions. In addition to core inference tools, the package
provides modules for parameter recovery, posterior predictive checks, and
model comparison, facilitating the study of a wide range of cognitive
processes in tasks involving perceptual decision making, memory retrieval,
and value-based decision making. Key methods implemented in the package
are described in Ratcliff (1978) <doi:10.1037/0033-295X.85.2.59>, Usher
and McClelland (2001) <doi:10.1037/0033-295X.108.3.550>, Brown and
Heathcote (2008) <doi:10.1016/j.cogpsych.2007.12.002>, Tillman, Van Zandt
and Logan (2020) <doi:10.3758/s13423-020-01719-6>, Wieschen, Voss and
Radev (2020) <doi:10.20982/tqmp.16.2.p120>, Csilléry, François and Blum
(2012) <doi:10.1111/j.2041-210X.2011.00179.x>, Beaumont (2019)
<doi:10.1146/annurev-statistics-030718-105212>, and Sainsbury-Dale,
Zammit-Mangion and Huser (2024) <doi:10.1080/00031305.2023.2249522>.

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
