%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AID
%global packver   2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8
Release:          1%{?dist}%{?buildtag}
Summary:          Box-Cox Power Transformation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-CRAN-nortest 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-meta 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tseries 
Requires:         R-CRAN-nortest 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-psych 
Requires:         R-stats 
Requires:         R-CRAN-meta 
Requires:         R-CRAN-stringr 

%description
Performs Box-Cox power transformation for a single non-normal variable,
ANOVA (Dag and Ilk, 2017) <doi:10.1080/03610918.2016.1204458> and Linear
Models via different estimation techniques: maximum likelihood estimation,
least square estimation, goodness-of-fit tests (Asar et al., 2017)
<doi:10.1080/03610918.2014.957839>, artificial covariate (Dag et al.,
2014) <doi:10.1080/03610918.2012.744042>, meta analysis (Yilmaz and Dag,
2022) <doi:10.28979/jarnas.1037343>. It also performs graphical
approaches, assesses the success of the transformation via tests and
plots, computes mean and confidence interval for back transformed data.

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
