%global packname  AICcmodavg
%global packver   2.3-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model Selection and Multimodel Inference Based on (Q)AIC(c)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-lattice 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-nlme 
BuildRequires:    R-stats4 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-unmarked 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-xtable 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-lattice 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-nlme 
Requires:         R-stats4 
Requires:         R-survival 
Requires:         R-CRAN-unmarked 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-xtable 

%description
Functions to implement model selection and multimodel inference based on
Akaike's information criterion (AIC) and the second-order AIC (AICc), as
well as their quasi-likelihood counterparts (QAIC, QAICc) from various
model object classes.  The package implements classic model averaging for
a given parameter of interest or predicted values, as well as a shrinkage
version of model averaging parameter estimates or effect sizes.  The
package includes diagnostics and goodness-of-fit statistics for certain
model types including those of 'unmarkedFit' classes estimating
demographic parameters after accounting for imperfect detection
probabilities.  Some functions also allow the creation of model selection
tables for Bayesian models of the 'bugs', 'rjags', and 'jagsUI' classes.
Functions also implement model selection using BIC.  Objects following
model selection and multimodel inference can be formatted to LaTeX using
'xtable' methods included in the package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
