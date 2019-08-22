%global packname  aster
%global packver   1.0-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Aster Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-stats 
Requires:         R-CRAN-trust 
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
(aster transform of usual parameterization). There are also random effects
versions of these models.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
