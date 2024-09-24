%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modsem
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Interaction (and Moderation) Analysis in Structural Equation Models (SEM)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-mvnfast 
Requires:         R-stats 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 

%description
Estimation of interaction (i.e., moderation) effects between latent
variables in structural equation models (SEM). The supported methods are:
The constrained approach (Algina & Moulder, 2001). The unconstrained
approach (Marsh et al., 2004). The residual centering approach (Little et
al., 2006). The double centering approach (Lin et al., 2010). The latent
moderated structural equations (LMS) approach (Klein & Moosbrugger, 2000).
The quasi-maximum likelihood (QML) approach (Klein & Muthén, 2007)
(temporarily unavailable) The constrained- unconstrained, residual- and
double centering- approaches are estimated via 'lavaan' (Rosseel, 2012),
whilst the LMS- and QML- approaches are estimated via by modsem it self.
Alternatively model can be estimated via 'Mplus' (Muthén & Muthén,
1998-2017). References: Algina, J., & Moulder, B. C. (2001).
<doi:10.1207/S15328007SEM0801_3>. "A note on estimating the Jöreskog-Yang
model for latent variable interaction using 'LISREL' 8.3." Klein, A., &
Moosbrugger, H. (2000). <doi:10.1007/BF02296338>. "Maximum likelihood
estimation of latent interaction effects with the LMS method." Klein, A.
G., & Muthén, B. O. (2007). <doi:10.1080/00273170701710205>.
"Quasi-maximum likelihood estimation of structural equation models with
multiple interaction and quadratic effects." Lin, G. C., Wen, Z., Marsh,
H. W., & Lin, H. S. (2010). <doi:10.1080/10705511.2010.488999>.
"Structural equation models of latent interactions: Clarification of
orthogonalizing and double-mean-centering strategies." Little, T. D.,
Bovaird, J. A., & Widaman, K. F. (2006). <doi:10.1207/s15328007sem1304_1>.
"On the merits of orthogonalizing powered and product terms: Implications
for modeling interactions among latent variables." Marsh, H. W., Wen, Z.,
& Hau, K. T. (2004). <doi:10.1037/1082-989X.9.3.275>. "Structural equation
models of latent interactions: evaluation of alternative estimation
strategies and indicator construction." Muthén, L.K. and Muthén, B.O.
(1998-2017). "'Mplus' User’s Guide.  Eighth Edition."
<https://www.statmodel.com/>. Rosseel Y (2012).
<doi:10.18637/jss.v048.i02>. "'lavaan': An R Package for Structural
Equation Modeling."

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
