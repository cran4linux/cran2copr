%global packname  misreport
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Statistical Analysis of Misreporting on Sensitive SurveyQuestions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv >= 2014.2.1
BuildRequires:    R-CRAN-mvtnorm >= 1.0.5
BuildRequires:    R-CRAN-VGAM >= 1.0.2
Requires:         R-CRAN-numDeriv >= 2014.2.1
Requires:         R-CRAN-mvtnorm >= 1.0.5
Requires:         R-CRAN-VGAM >= 1.0.2

%description
Enables investigation of the predictors of misreporting on sensitive
survey questions through a multivariate list experiment regression method.
The method permits researchers to model whether a survey respondent's
answer to the sensitive item in a list experiment is different from his or
her answer to an analogous direct question.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
