%global __brp_check_rpaths %{nil}
%global packname  adana
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Nature-Inspired Algorithms for Hybrid Genetic Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.optimx 
Requires:         R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.optimx 

%description
The Genetic Algorithm (GA) is a type of optimization method of
Evolutionary Algorithms. It uses the biologically inspired operators such
as mutation, crossover, selection and replacement.Because of their global
search and robustness abilities, GAs have been widely utilized in machine
learning, expert systems, data science, engineering, life sciences and
many other areas of research and business. However, the regular GAs need
the techniques to improve their efficiency in computing time and
performance in finding global optimum using some adaptation and
hybridization strategies. The adaptive GAs (AGA) increase the convergence
speed and success of regular GAs by setting the parameters crossover and
mutation probabilities dynamically. The hybrid GAs combine the exploration
strength of a stochastic GAs with the exact convergence ability of any
type of deterministic local search algorithms such as simulated-annealing,
in addition to other nature-inspired algorithms such as ant colony
optimization, particle swarm optimization etc. The package 'adana'
includes a rich working environment with its many functions that make
possible to build and work regular GA, adaptive GA, hybrid GA and hybrid
adaptive GA for any kind of optimization problems. Cebeci, Z. (2021, ISBN:
9786254397448).

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
