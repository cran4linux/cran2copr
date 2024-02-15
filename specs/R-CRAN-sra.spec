%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sra
%global packver   0.1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Selection Response Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-stats4 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-stats4 
Requires:         R-graphics 

%description
Artificial selection through selective breeding is an efficient way to
induce changes in traits of interest in experimental populations. This
package (sra) provides a set of tools to analyse artificial-selection
response datasets. The data typically feature for several generations the
average value of a trait in a population, the variance of the trait, the
population size and the average value of the parents that were chosen to
breed. Sra implements two families of models aiming at describing the
dynamics of the genetic architecture of the trait during the selection
response. The first family relies on purely descriptive (phenomenological)
models, based on an autoregressive framework. The second family provides
different mechanistic models, accounting e.g. for inbreeding, mutations,
genetic and environmental canalization, or epistasis. The parameters
underlying the dynamics of the time series are estimated by maximum
likelihood. The sra package thus provides (i) a wrapper for the R
functions mle() and optim() aiming at fitting in a convenient way a
predetermined set of models, and (ii) some functions to plot and analyze
the output of the models.

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
