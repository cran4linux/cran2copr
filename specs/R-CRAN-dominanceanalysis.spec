%global packname  dominanceanalysis
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Dominance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Dominance analysis is a method that allows to compare the relative
importance of predictors in multiple regression models: ordinary least
squares, generalized linear models and hierarchical linear models. The
main principles and methods of dominance analysis are described in
Budescu, D. V. (1993) <doi:10.1037/0033-2909.114.3.542> and Azen, R., &
Budescu, D. V. (2003) <doi:10.1037/1082-989X.8.2.129> for ordinary least
squares regression. Subsequently, the extensions for multivariate
regression, logistic regression and hierarchical linear models were
described in Azen, R., & Budescu, D. V. (2006)
<doi:10.3102/10769986031002157>, Azen, R., & Traxel, N. (2009)
<doi:10.3102/1076998609332754> and Luo, W., & Azen, R. (2013)
<doi:10.3102/1076998612458319>, respectively.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
