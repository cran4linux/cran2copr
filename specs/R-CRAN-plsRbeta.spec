%global packname  plsRbeta
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          3%{?dist}%{?buildtag}
Summary:          Partial Least Squares Regression for Beta Regression Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-plsRglm 
BuildRequires:    R-CRAN-betareg 
BuildRequires:    R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-boot 
Requires:         R-CRAN-Formula 
Requires:         R-MASS 
Requires:         R-CRAN-plsRglm 
Requires:         R-CRAN-betareg 
Requires:         R-methods 

%description
Provides Partial least squares Regression for (weighted) beta regression
models (Bertrand 2013, <http://journal-sfds.fr/article/view/215>) and
k-fold cross-validation of such models using various criteria. It allows
for missing data in the explanatory variables. Bootstrap confidence
intervals constructions are also available.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
