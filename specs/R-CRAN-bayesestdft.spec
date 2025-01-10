%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bayesestdft
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating the Degrees of Freedom of the Student's t-Distribution under a Bayesian Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.4
Requires:         R-core >= 4.0.4
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-dplyr 

%description
A Bayesian framework to estimate the Student's t-distribution's degrees of
freedom is developed. Markov Chain Monte Carlo sampling routines are
developed as in <doi:10.3390/axioms11090462> to sample from the posterior
distribution of the degrees of freedom. A random walk Metropolis algorithm
is used for sampling when Jeffrey's and Gamma priors are endowed upon the
degrees of freedom. In addition, the Metropolis-adjusted Langevin
algorithm for sampling is used under the Jeffrey's prior specification.
The Log-normal prior over the degrees of freedom is posed as a viable
choice with comparable performance in simulations and real-data
application, against other prior choices, where an Elliptical Slice
Sampler is used to sample from the concerned posterior.

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
