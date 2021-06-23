%global __brp_check_rpaths %{nil}
%global packname  detectseparation
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Detect and Check for Separation and Infinite Maximum Likelihood Estimates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-ROI.plugin.lpsolve 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-pkgload 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-ROI.plugin.lpsolve 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-pkgload 

%description
Provides pre-fit and post-fit methods for detecting separation and
infinite maximum likelihood estimates in generalized linear models with
categorical responses. The pre-fit methods apply on binomial-response
generalized liner models such as logit, probit and cloglog regression, and
can be directly supplied as fitting methods to the glm() function. They
solve the linear programming problems for the detection of separation
developed in Konis (2007,
<https://ora.ox.ac.uk/objects/uuid:8f9ee0d0-d78e-4101-9ab4-f9cbceed2a2a>)
using 'ROI' <https://cran.r-project.org/package=ROI> or 'lpSolveAPI'
<https://cran.r-project.org/package=lpSolveAPI>. The post-fit methods
apply to models with categorical responses, including binomial-response
generalized linear models and multinomial-response models, such as
baseline category logits and adjacent category logits models; for example,
the models implemented in the 'brglm2'
<https://cran.r-project.org/package=brglm2> package. The post-fit methods
successively refit the model with increasing number of iteratively
reweighted least squares iterations, and monitor the ratio of the
estimated standard error for each parameter to what it has been in the
first iteration. According to the results in Lesaffre & Albert (1989,
<https://www.jstor.org/stable/2345845>), divergence of those ratios
indicates data separation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
