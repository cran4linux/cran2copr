%global __brp_check_rpaths %{nil}
%global packname  rdrobust
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Data-Driven Statistical Inference in Regression-Discontinuity Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MASS 

%description
Regression-discontinuity (RD) designs are quasi-experimental research
designs popular in social, behavioral and natural sciences. The RD design
is usually employed to study the (local) causal effect of a treatment,
intervention or policy. This package provides tools for data-driven
graphical and analytical statistical inference in RD designs: rdrobust()
to construct local-polynomial point estimators and robust confidence
intervals for average treatment effects at the cutoff in Sharp, Fuzzy and
Kink RD settings, rdbwselect() to perform bandwidth selection for the
different procedures implemented, and rdplot() to conduct exploratory data
analysis (RD plots).

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
