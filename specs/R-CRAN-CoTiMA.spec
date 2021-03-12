%global packname  CoTiMA
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Time Meta-Analysis ('CoTiMA')

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-MBESS >= 4.6.0
BuildRequires:    R-CRAN-openxlsx >= 4.2.2
BuildRequires:    R-graphics >= 4.0.3
BuildRequires:    R-base >= 4.0.3
BuildRequires:    R-grDevices >= 4.0.3
BuildRequires:    R-utils >= 3.6.2
BuildRequires:    R-stats >= 3.6.2
BuildRequires:    R-parallel >= 3.6.1
BuildRequires:    R-CRAN-ctsem >= 3.3.11
BuildRequires:    R-CRAN-OpenMx >= 2.18.1
BuildRequires:    R-CRAN-psych >= 1.9.12
BuildRequires:    R-CRAN-rootSolve >= 1.8.2
BuildRequires:    R-CRAN-foreach >= 1.5.1
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-crayon >= 1.3.4
BuildRequires:    R-CRAN-zcurve >= 1.0.7
BuildRequires:    R-CRAN-stringi >= 1.0.7
BuildRequires:    R-CRAN-doParallel >= 1.0.15
BuildRequires:    R-CRAN-expm >= 0.999
BuildRequires:    R-CRAN-lavaan >= 0.6
BuildRequires:    R-CRAN-RPushbullet >= 0.3.3
BuildRequires:    R-CRAN-scholar >= 0.2.0
Requires:         R-CRAN-MASS >= 7.3.51.4
Requires:         R-CRAN-MBESS >= 4.6.0
Requires:         R-CRAN-openxlsx >= 4.2.2
Requires:         R-graphics >= 4.0.3
Requires:         R-base >= 4.0.3
Requires:         R-grDevices >= 4.0.3
Requires:         R-utils >= 3.6.2
Requires:         R-stats >= 3.6.2
Requires:         R-parallel >= 3.6.1
Requires:         R-CRAN-ctsem >= 3.3.11
Requires:         R-CRAN-OpenMx >= 2.18.1
Requires:         R-CRAN-psych >= 1.9.12
Requires:         R-CRAN-rootSolve >= 1.8.2
Requires:         R-CRAN-foreach >= 1.5.1
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-crayon >= 1.3.4
Requires:         R-CRAN-zcurve >= 1.0.7
Requires:         R-CRAN-stringi >= 1.0.7
Requires:         R-CRAN-doParallel >= 1.0.15
Requires:         R-CRAN-expm >= 0.999
Requires:         R-CRAN-lavaan >= 0.6
Requires:         R-CRAN-RPushbullet >= 0.3.3
Requires:         R-CRAN-scholar >= 0.2.0

%description
Performs meta-analyses of correlation matrices of repeatedly measured
variables for studies with different time lags. As always, variables are
measured at discrete time points (e.g., today at 4pm, next week on Monday
etc.), which imposes a problem for meta-analysis of studies that
repeatedly measured the variables because the time lags between
measurement could vary across studies. However, so-called continuous time
math can be used to extrapolate or intrapolate the results from all
studies to any desired time lag. By this, effects obtained in studies that
used different time lags can be meta-analyzed. In a nutshell, 'CoTiMA'
fits models to empirical data using the structural equation model (SEM)
packages 'OpenMx' and 'CTSEM', the effects specified in a SEM are related
to parameters that are not directly included in the model (i.e.,
continuous time parameters; together, they represent the continuous time
structural equation model, 'ctsem') which is done in a fashion similar to
other SEM programs (e.g., like a = b × c to test for mediation in 'MPLUS')
using matrix algebra functions (e.g., matrix exponentiation, which is not
available in 'MPLUS'), and statistical model comparisons and significance
tests are performed on the continuous time parameter estimates. Of course,
extrapolating or intrapolating effects always rests on particular
assumptions. A critical assumption is the underlying causal model that
describes the process under investigation. For example, a causal system
that describes how a single variable that is measured repeatedly (e.g.,
X1, X2, X2, etc.) could propose that X1 affects X2, X2 affects X3 and so
forth. This is called a first order autoregressive structure and the model
which is used by default for a 'CoTiMA' of a single variable. In a
two-variable model of X and Y, the underlying 'CoTiMA' model is a
cross-lagged model with autoregressive effects for X and Y and, in
addition, a cross-lagged effect of Xt on Yt+1 and of Yt on Xt+1. More
complex models (e.g., including Xt on Yt+1 and Xt on Yt+2) could be
meta-analyzed, too, but they require user-specific adaptations. More
simple models (e.g., Xt on Yt+1 but not Yt on Xt+1) are easier to
implement and several specific models (e.g., Xt on Yt+1 exactly of the
same size as Yt on Xt+1) could be optionally requested. Usually,
researchers are interested in the sizes of these effects rather than the
correlations on which they are based. Thus, correlations of primary
studies serve as an input for 'CoTiMA' and synthesized (i.e.,
meta-analytically aggregated) effect sizes represent the output of
'CoTiMA'. Dormann, C., Guthier, C., & Cortina, J. M. (2019)
<doi:10.1177/1094428119847277>. Guthier, C., Dormann, C., & Voelkle, M. C.
(2020) <doi:10.1037/bul0000304>.

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
