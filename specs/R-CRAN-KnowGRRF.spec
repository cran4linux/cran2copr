%global packname  KnowGRRF
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Knowledge-Based Guided Regularized Random Forest

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-RRF 
BuildRequires:    R-CRAN-PRROC 
BuildRequires:    R-MASS 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-RRF 
Requires:         R-CRAN-PRROC 
Requires:         R-MASS 

%description
Random Forest (RF) and Regularized Random Forest can be used for feature
selection. Moreover, by Guided Regularized Random Forest,
statistical-based weights are used to guide the regularization of random
forest and further used for feature selection. This package can integrate
prior information from multiple domains (statistical based and knowledge
domain) to guide the regularization of random forest and feature
selection. For more details, see reference: Guan X., Liu L. (2018)
<doi:10.1007/978-3-319-78759-6_1>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
