%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statAPA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          APA 7th Edition Statistical Tables, Plots, and Multilevel Model Reports

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-car >= 3.1.0
BuildRequires:    R-CRAN-sandwich >= 3.0.0
BuildRequires:    R-CRAN-emmeans >= 1.8.0
BuildRequires:    R-CRAN-lme4 >= 1.1.30
BuildRequires:    R-CRAN-lmtest >= 0.9.40
BuildRequires:    R-CRAN-flextable >= 0.9.0
BuildRequires:    R-CRAN-officer >= 0.6.0
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-car >= 3.1.0
Requires:         R-CRAN-sandwich >= 3.0.0
Requires:         R-CRAN-emmeans >= 1.8.0
Requires:         R-CRAN-lme4 >= 1.1.30
Requires:         R-CRAN-lmtest >= 0.9.40
Requires:         R-CRAN-flextable >= 0.9.0
Requires:         R-CRAN-officer >= 0.6.0
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rlang 

%description
Produces publication-ready statistical tables and figures formatted
according to the 7th edition of the American Psychological Association
(APA) style guidelines. Supports descriptive statistics, t-tests, z-tests,
chi-square tests, Analysis of Variance (ANOVA), Analysis of Covariance
(ANCOVA), two-way ANOVA with simple effects, Multivariate Analysis of
Variance (MANOVA), robust and cluster-robust regression using
Heteroscedasticity-Consistent (HC) standard errors, post-hoc pairwise
comparisons, homoskedasticity and heteroscedasticity diagnostics including
the Non-Constant Variance (NCV) test, proportion tests, and multilevel
mixed-effects models with intraclass correlation coefficients (ICC) and
model-comparison tables. Output can be directed to the console, Microsoft
Word (via 'officer' and 'flextable'), or LaTeX. For APA style guidelines
see American Psychological Association (2020, ISBN:978-1-4338-3216-1).

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
