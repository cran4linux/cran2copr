%global packname  rpsychi
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Statistics for psychiatric research

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-gtools 

%description
The rpsychi offers a number of functions for psychiatry, psychiatric
nursing, clinical psychology. Functions are primarily for statistical
significance testing using published work. For example, you can conduct a
factorial analysis of variance (ANOVA), which requires only the mean,
standard deviation, and sample size for each cell, rather than the
individual data. This package covers fundamental statistical tests such as
t-test, chi-square test, analysis of variance, and multiple regression
analysis. With some exceptions, you can obtain effect size and its
confidence interval. These functions help you to obtain effect size from
published work, and then to conduct a priori power analysis or
meta-analysis, even if a researcher do not report effect size in a
published work.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
