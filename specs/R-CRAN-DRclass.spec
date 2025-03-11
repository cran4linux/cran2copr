%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DRclass
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Consider Ambiguity in Probabilistic Descriptions Using Density Ratio Classes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Consider ambiguity in probabilistic descriptions by replacing a parametric
probabilistic description of uncertainty by a non-parametric set of
probability distributions in the form of a Density Ratio Class. This is of
particular interest in Bayesian inference. The Density Ratio Class is
particularly suited for this purpose as it is invariant under Bayesian
inference, marginalization, and propagation through a deterministic model.
Here, invariant means that the result of the operation applied to a
Density Ratio Class is again a Density Ratio Class. In particular the
invariance under Bayesian inference thus enables iterative learning within
the same framework of Density Ratio Classes. The use of imprecise
probabilities in general, and Density Ratio Classes in particular, lead to
intervals of characteristics of probability distributions, such as
cumulative distribution functions, quantiles, and means. The package is
based on a sample of the distribution proportional to the upper bound of
the class. Typically this will be a sample from the posterior in Bayesian
inference. Based on such a sample, the package provides functions to
calculate lower and upper class boundaries and lower and upper bounds of
cumulative distribution functions, and quantiles. Rinderknecht, S.L.,
Albert, C., Borsuk, M.E., Schuwirth, N., Kuensch, H.R. and Reichert, P.
(2014) "The effect of ambiguous prior knowledge on Bayesian model
parameter inference and prediction." Environmental Modelling & Software.
62, 300-315, 2014. <doi:10.1016/j.envsoft.2014.08.020>. Sriwastava, A. and
Reichert, P. "Robust Bayesian Estimation of Value Function Parameters
using Imprecise Priors." Submitted.
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4973574>.

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
