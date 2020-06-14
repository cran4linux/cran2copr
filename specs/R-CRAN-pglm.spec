%global packname  pglm
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Panel Generalized Linear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-plm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-plm 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-Formula 

%description
Estimation of panel models for glm-like models: this includes binomial
models (logit and probit) count models (poisson and negbin) and ordered
models (logit and probit), as described in Baltagi (2013) Econometric
Analysis of Panel Data, ISBN-13:978-1-118-67232-7, Hsiao (2014) Analysis
of Panel Data <doi:10.1017/CBO9781139839327> and Croissant and Millo
(2018), Panel Data Econometrics with R, ISBN:978-1-118-94918-4.

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
%{rlibdir}/%{packname}/INDEX
