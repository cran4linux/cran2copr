%global packname  globalboosttest
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Testing the additional predictive value of high-dimensional data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8
Requires:         R-core >= 2.8
BuildArch:        noarch
BuildRequires:    R-CRAN-mboost >= 2.0.0
BuildRequires:    R-survival 
Requires:         R-CRAN-mboost >= 2.0.0
Requires:         R-survival 

%description
'globalboosttest' implements a permutation-based testing procedure to
globally test the (additional) predictive value of a large set of
predictors given that a small set of predictors is already available.
Currently, 'globalboosttest' supports binary outcomes (via logistic
regression) and survival outcomes (via Cox regression). It is based on
boosting regression as implemented in the package 'mboost'.

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
