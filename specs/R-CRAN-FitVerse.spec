%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FitVerse
%global packver   1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Distribution Fitting and Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-actuar >= 3.1.0
BuildRequires:    R-CRAN-lmomco >= 2.3.7
BuildRequires:    R-CRAN-evd >= 2.3.3
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-sn >= 2.1.0
BuildRequires:    R-CRAN-goftest >= 1.2.3
BuildRequires:    R-CRAN-fitdistrplus >= 1.1.0
BuildRequires:    R-CRAN-mc2d >= 0.1.18
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-actuar >= 3.1.0
Requires:         R-CRAN-lmomco >= 2.3.7
Requires:         R-CRAN-evd >= 2.3.3
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-sn >= 2.1.0
Requires:         R-CRAN-goftest >= 1.2.3
Requires:         R-CRAN-fitdistrplus >= 1.1.0
Requires:         R-CRAN-mc2d >= 0.1.18
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-tools 

%description
Provides a unified, user-friendly interface for fitting parametric
probability distributions to continuous univariate data. 'FitVerse'
supports 52 distribution families spanning symmetric, right-skewed,
heavy-tailed, bounded, and extreme-value shapes, and three estimation
methods: Maximum Likelihood Estimation (MLE), Method of Moments (MOM), and
L-Moments (L-MOM). Automatic best-fit selection is performed using AIC,
BIC, and goodness-of-fit tests (Kolmogorov-Smirnov, Anderson-Darling,
Cramer-von Mises (CvM)). Every fitted model produces a publication-quality
diagnostic plot: a histogram overlaid with the fitted density curve and
the estimated PDF formula annotated directly on the figure. An optional
interactive version is produced via 'plotly'. Additional tools include
bootstrap confidence intervals for parameter estimates and return levels,
batch fitting across multiple columns for automated workflows and
web-upload use cases, JSON serialisation for integration with 'Shiny' web
applications, and automated HTML/PDF report generation. 'FitVerse' is
designed to support data characterisation in survey sampling, hydrology,
and actuarial workflows, where identifying the underlying distribution of
a variable is a prerequisite for downstream modelling and inference.
L-moment estimation follows Hosking (1990)
<doi:10.1111/j.2517-6161.1990.tb01775.x> and Hosking and Wallis (1997,
ISBN:9780521430456). Model selection via AIC follows Akaike (1974)
<doi:10.1109/TAC.1974.1100705> and via BIC follows Schwarz (1978)
<doi:10.1214/aos/1176344136>. Bootstrap confidence intervals follow Efron
and Hastie (2016, ISBN:9781107149892).

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
