%global packname  crch
%global packver   1.0-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          1%{?dist}
Summary:          Censored Regression with Conditional Heteroscedasticity

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-ordinal 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-scoringRules 
Requires:         R-stats 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-ordinal 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-scoringRules 

%description
Different approaches to censored or truncated regression with conditional
heteroscedasticity are provided. First, continuous distributions can be
used for the (right and/or left censored or truncated) response with
separate linear predictors for the mean and variance. Second, cumulative
link models for ordinal data (obtained by interval-censoring continuous
data) can be employed for heteroscedastic extended logistic regression
(HXLR). In the latter type of models, the intercepts depend on the
thresholds that define the intervals.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
