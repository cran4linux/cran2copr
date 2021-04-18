%global packname  nimble
%global packver   0.11.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11.0
Release:          1%{?dist}%{?buildtag}
Summary:          MCMC, Particle Filtering, and Programmable Hierarchical Modeling

License:          BSD_3_clause + file LICENSE | GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-R6 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-R6 

%description
A system for writing hierarchical statistical models largely compatible
with 'BUGS' and 'JAGS', writing nimbleFunctions to operate models and do
basic R-style math, and compiling both models and nimbleFunctions via
custom-generated C++. 'NIMBLE' includes default methods for MCMC, Monte
Carlo Expectation Maximization, and some other tools. The nimbleFunction
system makes it easy to do things like implement new MCMC samplers from R,
customize the assignment of samplers to different parts of a model from R,
and compile the new samplers automatically via C++ alongside the samplers
'NIMBLE' provides. 'NIMBLE' extends the 'BUGS'/'JAGS' language by making
it extensible: New distributions and functions can be added, including as
calls to external compiled code. Although most people think of MCMC as the
main goal of the 'BUGS'/'JAGS' language for writing models, one can use
'NIMBLE' for writing arbitrary other kinds of model-generic algorithms as
well. A full User Manual is available at <https://r-nimble.org>.

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
