%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QAEnsemble
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Ensemble Quadratic and Affine Invariant Markov Chain Monte Carlo

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
The Ensemble Quadratic and Affine Invariant Markov chain Monte Carlo
algorithms provide an efficient way to perform Bayesian inference in
difficult parameter space geometries. The Ensemble Quadratic Monte Carlo
algorithm was developed by Militzer (2023) <doi:10.3847/1538-4357/ace1f1>.
The Ensemble Affine Invariant algorithm was developed by Goodman and Weare
(2010) <doi:10.2140/camcos.2010.5.65> and it was implemented in Python by
Foreman-Mackey et al (2013) <doi:10.48550/arXiv.1202.3665>. The Quadratic
Monte Carlo method was shown to perform better than the Affine Invariant
method in the paper by Militzer (2023) <doi:10.3847/1538-4357/ace1f1> and
the Quadratic Monte Carlo method is the default method used. The Chen-Shao
Highest Posterior Density Estimation algorithm is used for obtaining
credible intervals and the potential scale reduction factor diagnostic is
used for checking the convergence of the chains.

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
