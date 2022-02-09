%global __brp_check_rpaths %{nil}
%global packname  indirect
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Elicitation of Independent Conditional Means Priors for Generalised Linear Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-gplots 

%description
Functions are provided to facilitate prior elicitation for Bayesian
generalised linear models using independent conditional means priors. The
package supports the elicitation of multivariate normal priors for
generalised linear models. The approach can be applied to indirect
elicitation for a generalised linear model that is linear in the
parameters. The package is designed such that the facilitator executes
functions within the R console during the elicitation session to provide
graphical and numerical feedback at each design point. Various
methodologies for eliciting fractiles (equivalently, percentiles or
quantiles) are supported, including versions of the approach of Hosack et
al. (2017) <doi:10.1016/j.ress.2017.06.011>. For example, experts may be
asked to provide central credible intervals that correspond to a certain
probability. Or experts may be allowed to vary the probability allocated
to the central credible interval for each design point. Additionally, a
median may or may not be elicited.

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
