%global __brp_check_rpaths %{nil}
%global packname  overdisp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Overdispersion in Count Data Multiple Regression Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Detection of overdispersion in count data for multiple regression
analysis. Log-linear count data regression is one of the most popular
techniques for predictive modeling where there is a non-negative discrete
quantitative dependent variable. In order to ensure the inferences from
the use of count data models are appropriate, researchers may choose
between the estimation of a Poisson model and a negative binomial model,
and the correct decision for prediction from a count data estimation is
directly linked to the existence of overdispersion of the dependent
variable, conditional to the explanatory variables. Based on the studies
of Cameron and Trivedi (1990) <doi:10.1016/0304-4076(90)90014-K> and
Cameron and Trivedi (2013, ISBN:978-1107667273), the overdisp() command is
a contribution to researchers, providing a fast and secure solution for
the detection of overdispersion in count data. Another advantage is that
the installation of other packages is unnecessary, since the command runs
in the basic R language.

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
