%global packname  ANOVA.TFNs
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          One-Way Analysis of Variance Based on Triangular Fuzzy Numbers

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FuzzyNumbers 
Requires:         R-CRAN-FuzzyNumbers 

%description
Long formulas and complex computations are two disadvantage of the
extended ANOVA approach where the observed data are fuzzy rather that
crisp; for more details see Parchami et al. (2017)
<doi:10.1007/s40747-017-0046-8>. Package 'ANOVA.TFNs' can help to the
applied users to overcome these two challenges. The most important
functions in package 'ANOVA.TFNs' is FANOVA() which easily draw all
membership functions of fuzzy numbers, report observed statistics in fuzzy
ANOVA table, calculate the p-value and final result for Fuzzy ANOVA test
at the certain significance level.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
