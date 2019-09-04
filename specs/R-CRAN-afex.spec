%global packname  afex
%global packver   0.25-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.25.1
Release:          1%{?dist}
Summary:          Analysis of Factorial Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lmerTest >= 3.0.0
BuildRequires:    R-CRAN-lme4 >= 1.1.8
BuildRequires:    R-CRAN-pbkrtest >= 0.4.1
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-lmerTest >= 3.0.0
Requires:         R-CRAN-lme4 >= 1.1.8
Requires:         R-CRAN-pbkrtest >= 0.4.1
Requires:         R-CRAN-car 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 

%description
Convenience functions for analyzing factorial experiments using ANOVA or
mixed models. aov_ez(), aov_car(), and aov_4() allow specification of
between, within (i.e., repeated-measures), or mixed (i.e., split-plot)
ANOVAs for data in long format (i.e., one observation per row),
automatically aggregating multiple observations per individual and cell of
the design. mixed() fits mixed models using lme4::lmer() and computes
p-values for all fixed effects using either Kenward-Roger or Satterthwaite
approximation for degrees of freedom (LMM only), parametric bootstrap
(LMMs and GLMMs), or likelihood ratio tests (LMMs and GLMMs). afex_plot()
provides a high-level interface for interaction or one-way plots using
ggplot2, combining raw data and model estimates. afex uses type 3 sums of
squares as default (imitating commercial statistical software).

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
