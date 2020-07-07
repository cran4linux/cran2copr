%global packname  xgb2sql
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Convert Trained 'XGBoost' Model to SQL Query

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-xgboost >= 0.81.0.1
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-xgboost >= 0.81.0.1

%description
This tool enables in-database scoring of 'XGBoost' models built in R, by
translating trained model objects into SQL query. 'XGBoost'
<https://xgboost.readthedocs.io/en/latest/index.html> provides parallel
tree boosting (also known as gradient boosting machine, or GBM) algorithms
in a highly efficient, flexible and portable way. GBM algorithm is
introduced by Friedman (2001) <doi:10.1214/aos/1013203451>, and more
details on 'XGBoost' can be found in Chen & Guestrin (2016)
<doi:10.1145/2939672.2939785>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
