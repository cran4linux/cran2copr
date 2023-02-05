%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dsmmR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation and Simulation of Drifting Semi-Markov Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DiscreteWeibull 
Requires:         R-CRAN-DiscreteWeibull 

%description
Performs parametric and non-parametric estimation and simulation of
drifting semi-Markov processes. The definition of parametric and
non-parametric model specifications is also possible. Furthermore, three
different types of drifting semi-Markov models are considered. These
models differ in the number of transition matrices and sojourn time
distributions used for the computation of a number of semi-Markov kernels,
which in turn characterize the drifting semi-Markov kernel. For the
parametric model estimation and specification, several discrete
distributions are considered for the sojourn times: Uniform, Poisson,
Geometric, Discrete Weibull and Negative Binomial. The non-parametric
model specification makes no assumptions about the shape of the sojourn
time distributions. Semi-Markov models are described in: Barbu, V.S.,
Limnios, N. (2008) <doi:10.1007/978-0-387-73173-5>. Drifting Markov models
are described in: Vergne, N. (2008) <doi:10.2202/1544-6115.1326>.
Reliability indicators of Drifting Markov models are described in: Barbu,
V. S., Vergne, N. (2019) <doi:10.1007/s11009-018-9682-8>.

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
