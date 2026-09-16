%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  oneway
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          One-Way Statistical Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-normality 
BuildRequires:    R-CRAN-outlying 
BuildRequires:    R-CRAN-varequal 
Requires:         R-CRAN-normality 
Requires:         R-CRAN-outlying 
Requires:         R-CRAN-varequal 

%description
Performs one-way tests of assumptions (normality and homoscedasticity),
analysis of variance, robust and nonparametric alternatives, multiple
comparison procedures, effect size estimators, confidence intervals, and
descriptive summaries. Functions are designed with a consistent interface
to support reproducible and user-friendly statistical workflows. For more
details see Howell (2010, ISBN:978-0-495-59784-1), Zar (2014,
ISBN:978-0-13-100846-5), Hollander et al. (2014, ISBN:978-0-470-38737-5),
Montgomery (2017, ISBN:978-1-119-11347-8), Lakens (2013)
<doi:10.3389/fpsyg.2013.00863>, and Piepho (2004)
<doi:10.1198/1061860043515>.

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
