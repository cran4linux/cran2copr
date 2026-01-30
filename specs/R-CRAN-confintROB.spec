%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  confintROB
%global packver   1.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Confidence Intervals for Robust and Classical Linear Mixed Model Estimators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 

%description
The main function calculates confidence intervals (CI) for Mixed Models,
utilizing both classical estimators from the lmer() function in the 'lme4'
package and robust estimators from the rlmer() function in the 'robustlmm'
package, as well as the varComprob() function in the 'robustvarComp'
package. Three methods are available: the classical Wald method, the wild
bootstrap, and the parametric bootstrap. Bootstrap methods offer
flexibility in obtaining lower and upper bounds through percentile or BCa
methods. More details are given in Mason, F., Cantoni, E., & Ghisletta, P.
(2021) <doi:10.5964/meth.6607> and Mason, F., Cantoni, E., & Ghisletta, P.
(2024) <doi:10.1037/met0000643>.

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
