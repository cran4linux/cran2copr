%global packname  inTrees
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Interpret Tree Ensembles

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RRF 
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
Requires:         R-CRAN-RRF 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-gbm 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-data.table 
Requires:         R-methods 

%description
For tree ensembles such as random forests, regularized random forests and
gradient boosted trees, this package provides functions for: extracting,
measuring and pruning rules; selecting a compact rule set; summarizing
rules into a learner; calculating frequent variable interactions;
formatting rules in latex code.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
