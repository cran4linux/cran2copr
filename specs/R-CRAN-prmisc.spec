%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  prmisc
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Miscellaneous Printing of Numeric and Statistical Output in R Markdown and Quarto Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch

%description
Miscellaneous printing of numeric or statistical results in R Markdown or
Quarto documents according to guidelines of the "Publication Manual" of
the American Psychological Association (2020, ISBN: 978-1-4338-3215-4).
These guidelines are usually referred to as APA style
(<https://apastyle.apa.org/>) and include specific rules on the formatting
of numbers and statistical test results. APA style has to be implemented
when submitting scientific reports in a wide range of research fields,
especially in the social sciences. The default output of numbers in the R
console or R Markdown and Quarto documents does not meet the APA style
requirements, and reformatting results manually can be cumbersome and
error-prone. This package covers the automatic conversion of R objects to
textual representations that meet the APA style requirements, which can be
included in R Markdown or Quarto documents. It covers some basic
statistical tests (t-test, ANOVA, correlation, chi-squared test, Wilcoxon
test) as well as some basic number printing manipulations (formatting
p-values, removing leading zeros for numbers that cannot be greater than
one, and others). Other packages exist for formatting numbers and tests
according to the APA style guidelines, such as 'papaja'
(<https://cran.r-project.org/package=papaja>) and 'apa'
(<https://cran.r-project.org/package=apa>), but they do not offer all
convenience functionality included in 'prmisc'. The vignette has an
overview of most of the functions included in the package.

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
