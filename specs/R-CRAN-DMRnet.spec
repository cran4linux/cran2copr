%global packname  DMRnet
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Delete or Merge Regressors Algorithms for Linear and LogisticModel Selection and High-Dimensional Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-grpreg 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 

%description
Model selection algorithms for regression and classification, where the
predictors can be numerical and categorical and the number of regressors
exceeds the number of observations. The selected model consists of a
subset of numerical regressors and partitions of levels of factors.
Aleksandra Maj-Kańska, Piotr Pokarowski and Agnieszka Prochenka (2015)
<doi:10.1214/15-EJS1050>. Piotr Pokarowski and Jan Mielniczuk (2015)
<http://www.jmlr.org/papers/volume16/pokarowski15a/pokarowski15a.pdf>.

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
