%global packname  cobalt
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          1%{?dist}
Summary:          Covariate Balance Tables and Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-backports >= 1.1.5
BuildRequires:    R-CRAN-gtable >= 0.3.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-crayon 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-backports >= 1.1.5
Requires:         R-CRAN-gtable >= 0.3.0
Requires:         R-grid 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-crayon 

%description
Generate balance tables and plots for covariates of groups preprocessed
through matching, weighting or subclassification, for example, using
propensity scores. Includes integration with 'MatchIt', 'twang',
'Matching', 'optmatch', 'CBPS', 'ebal', 'WeightIt', and 'designmatch' for
assessing balance on the output of their preprocessing functions. Users
can also specify data for balance assessment not generated through the
above packages. Also included are methods for assessing balance in
clustered or multiply imputed data sets or data sets with longitudinal
treatments.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/figures
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
