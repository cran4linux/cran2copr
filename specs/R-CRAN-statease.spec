%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  statease
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Simplified Statistical Analysis with Plain-English Interpretation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-car 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-shiny 

%description
A toolkit for common statistical analyses including descriptive
statistics, Student's t-tests (one-sample, independent, and paired),
one-way and two-way Analysis of Variance (ANOVA), Multivariate Analysis of
Variance (MANOVA), chi-square tests, Fisher's Exact Test, McNemar's Test,
correlation analysis, simple and multiple linear regression, logistic
regression, Friedman Test, and non-parametric tests (Mann-Whitney U,
Wilcoxon Signed Rank, and Kruskal-Wallis). Additional tools include
statistical power analysis and automated assumption checking. Each
function automatically interprets results in plain English, reporting
effect sizes, confidence intervals, and p-value interpretations. Post-hoc
tests are automatically applied following significant results. A master
function automatically detects the appropriate test based on the structure
of the input data. Methods are based on Cohen, J. (1988)
<doi:10.4324/9780203771587>, Tukey, J. W. (1949) <doi:10.2307/3001913>,
and Shapiro and Wilk (1965) <doi:10.2307/2333709>.

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
