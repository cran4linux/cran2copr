%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  agriDQ
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Data Quality Checks and Statistical Assumption Testing for Agricultural Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-stringdist 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-car 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-stringdist 

%description
Provides a comprehensive pipeline for data quality checks and statistical
assumption diagnostics in agricultural experimental data. Functions cover
outlier detection using Interquartile Range (IQR) fence, Z-score, modified
Z-score (Hampel identifier), Grubbs test and Dixon Q-test with consensus
flagging; missing data pattern analysis and mechanism classification
(Missing Completely At Random/Missing At Random/Missing Not At Random
(MCAR/MAR/MNAR)) via Little's test; normality testing using Shapiro-Wilk,
Anderson-Darling, Kolmogorov-Smirnov, Lilliefors, Pearson chi-square and
Jarque-Bera tests; homogeneity of variance via Bartlett, Levene and
Fligner-Killeen tests; independence of errors via Durbin-Watson,
Breusch-Godfrey and Wald-Wolfowitz runs tests; experimental design
validation for Completely Randomised Design (CRD), Randomised Complete
Block Design (RCBD), Latin Square Design (LSD) and factorial designs;
qualitative variable consistency checks; and automated HyperText Markup
Language (HTML) report generation. Designed to align with Findable,
Accessible, Interoperable and Reusable (FAIR) data principles. Methods
follow Gomez and Gomez (1984, ISBN:978-0471870920) and Montgomery (2017,
ISBN:978-1119492443).

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
