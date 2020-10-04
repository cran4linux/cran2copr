%global packname  aster2
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Aster Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-stats 

%description
Aster models are exponential family regression models for life history
analysis.  They are like generalized linear models except that elements of
the response vector can have different families (e. g., some Bernoulli,
some Poisson, some zero-truncated Poisson, some normal) and can be
dependent, the dependence indicated by a graphical structure. Discrete
time survival analysis, zero-inflated Poisson regression, and generalized
linear models that are exponential family (e. g., logistic regression and
Poisson regression with log link) are special cases. Main use is for data
in which there is survival over discrete time periods and there is
additional data about what happens conditional on survival (e. g., number
of offspring).  Uses the exponential family canonical parameterization
(aster transform of usual parameterization). Unlike the aster package,
this package does dependence groups (nodes of the graph need not be
conditionally independent given their predecessor node), including
multinomial and two-parameter normal as families.  Thus this package also
generalizes mark-capture-recapture analysis.

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
%{rlibdir}/%{packname}/makedata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
