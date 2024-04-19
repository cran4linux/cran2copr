%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmMisrep
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Linear Models Adjusting for Misrepresentation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-poisson.glm.mix 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-poisson.glm.mix 
Requires:         R-stats 

%description
Fit Generalized Linear Models to continuous and count outcomes, as well as
estimate the prevalence of misrepresentation of an important binary
predictor. Misrepresentation typically arises when there is an incentive
for the binary factor to be misclassified in one direction (e.g., in
insurance settings where policy holders may purposely deny a risk status
in order to lower the insurance premium). This is accomplished by treating
a subset of the response variable as resulting from a mixture
distribution. Model parameters are estimated via the Expectation
Maximization algorithm and standard errors of the estimates are obtained
from closed forms of the Observed Fisher Information. For an introduction
to the models and the misrepresentation framework, see Xia et. al., (2023)
<https://variancejournal.org/article/73151-maximum-likelihood-approaches-to-misrepresentation-models-in-glm-ratemaking-model-comparisons>.

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
