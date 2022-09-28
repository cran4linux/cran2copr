%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ContRespPP
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Probability for a Continuous Response with an ANOVA Structure

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A Bayesian approach to using predictive probability in an ANOVA construct
with a continuous normal response, when threshold values must be obtained
for the question of interest to be evaluated as successful (Sieck and
Christensen (2021) <doi:10.1002/qre.2802>). The Bayesian Mission Mean
(BMM) is used to evaluate a question of interest (that is, a mean that
randomly selects combination of factor levels based on their probability
of occurring instead of averaging over the factor levels, as in the grand
mean). Under this construct, in contrast to a Gibbs sampler (or
Metropolis-within-Gibbs sampler), a two-stage sampling method is required.
The nested sampler determines the conditional posterior distribution of
the model parameters, given Y, and the outside sampler determines the
marginal posterior distribution of Y (also commonly called the predictive
distribution for Y). This approach provides a sample from the joint
posterior distribution of Y and the model parameters, while also
accounting for the threshold value that must be obtained in order for the
question of interest to be evaluated as successful.

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
