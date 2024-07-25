%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  logitr
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Logit Models w/Preference & WTP Space Utility Parameterizations

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-randtoolbox 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Fast estimation of multinomial (MNL) and mixed logit (MXL) models in R.
Models can be estimated using "Preference" space or "Willingness-to-pay"
(WTP) space utility parameterizations. Weighted models can also be
estimated. An option is available to run a parallelized multistart
optimization loop with random starting points in each iteration, which is
useful for non-convex problems like MXL models or models with WTP space
utility parameterizations. The main optimization loop uses the 'nloptr'
package to minimize the negative log-likelihood function. Additional
functions are available for computing and comparing WTP from both
preference space and WTP space models and for predicting expected choices
and choice probabilities for sets of alternatives based on an estimated
model. Mixed logit models can include uncorrelated or correlated
heterogeneity covariances and are estimated using maximum simulated
likelihood based on the algorithms in Train (2009)
<doi:10.1017/CBO9780511805271>. More details can be found in Helveston
(2023) <doi:10.18637/jss.v105.i10>.

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
