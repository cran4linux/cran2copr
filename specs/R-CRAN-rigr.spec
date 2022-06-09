%global __brp_check_rpaths %{nil}
%global packname  rigr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Regression, Inference, and General Data Analysis Tools in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-sandwich 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
A set of tools to streamline data analysis. Learning both R and
introductory statistics at the same time can be challenging, and so we
created 'rigr' to facilitate common data analysis tasks and enable
learners to focus on statistical concepts. We provide easy-to-use
interfaces for descriptive statistics, one- and two-sample inference, and
regression analyses. 'rigr' output includes key information while omitting
unnecessary details that can be confusing to beginners.
Heteroscedasticity-robust ("sandwich") standard errors are returned by
default, and multiple partial F-tests and tests for contrasts are easy to
specify. A single regression function can fit both linear and generalized
linear models, allowing students to more easily make connections between
different classes of models.

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
