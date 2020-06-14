%global packname  rdrobust
%global packver   0.99.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.8
Release:          2%{?dist}
Summary:          Robust Data-Driven Statistical Inference inRegression-Discontinuity Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-ggplot2 

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

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
