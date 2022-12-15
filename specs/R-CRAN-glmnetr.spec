%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  glmnetr
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Relaxed Lasso Model for Data Which Might Have Long Run Times Using 'glmnet'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Matrix 

%description
For some datasets, for example when the design matrix is not of full rank,
'glmnet' may have very long run times when fitting the relaxed lasso
model, in particular when fitting a Cox based model, making it difficult
to get solutions either from glmnet() or cv.glmnet().  In this package,
'glmnetr', we provide a workaround and solve for the non penalized relaxed
model where gamma=0 for model structures analogue to R functions like
glm() or coxph() of the survival package.  If you are not fitting relaxed
lasso models, or if you are able to get convergence using 'glmnet', then
this package may not be of much benefit to you.  Note, while this package
may allow one to fit relaxed lasso models that have difficulties
converging using 'glmnet', this package does not afford the full function
and versatility of 'glmnet'. In addition to fitting the relaxed lasso
model this package also includes the function cv.glmnetr() to perform a
cross validation to identify hyper-parameters for a lasso fit, much like
the cv.glmnet() function of the 'glmnet' package.  Additionally, the
package includes the function nested.glmnetr() to perform a nested cross
validation to assess the fit of a cross validated derived lasso model fit.
If though you are fitting not a relaxed lasso model but an elastic-net
model, then the R-packages 'nestedcv'
<https://cran.r-project.org/package=nestedcv>, 'glmnetSE'
<https://cran.r-project.org/package=glmnetSE> or others may provide
greater functionality when performing a nested CV. As with the 'glmnet'
package, this package passes most relevant output to the output object and
tabular and graphical summaries can be generated using the summary and
plot functions.  Use of the 'glmnetr' has many similarities to the
'glmnet' package and it is recommended that the user of 'glmnetr' first
become familiar with the 'glmnet' package
<https://cran.r-project.org/package=glmnet>, with the "An Introduction to
'glmnet'" and "The Relaxed Lasso" being especially helpful in this regard.

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
