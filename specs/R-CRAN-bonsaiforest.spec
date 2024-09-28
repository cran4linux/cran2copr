%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bonsaiforest
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Shrinkage Based Forest Plots

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-brms >= 2.22.0
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-vdiffr 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-brms >= 2.22.0
Requires:         R-CRAN-broom 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-splines2 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-vdiffr 

%description
Subgroup analyses are routinely performed in clinical trial analyses. From
a methodological perspective, two key issues of subgroup analyses are
multiplicity (even if only predefined subgroups are investigated) and the
low sample sizes of subgroups which lead to highly variable estimates, see
e.g. Yusuf et al (1991) <doi:10.1001/jama.1991.03470010097038>.  This
package implements subgroup estimates based on Bayesian shrinkage priors,
see Carvalho et al (2019)
<https://proceedings.mlr.press/v5/carvalho09a.html>. In addition,
estimates based on penalized likelihood inference are available, based on
Simon et al (2011) <doi:10.18637/jss.v039.i05>. The corresponding
shrinkage based forest plots address the aforementioned issues and can
complement standard forest plots in practical clinical trial analyses.

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
