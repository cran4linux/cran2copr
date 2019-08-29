%global packname  galgo
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Genetic Algorithms for Multivariate Statistical Models fromLarge-Scale Functional Genomics Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-R.oo 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-rpart 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-MASS 
Requires:         R-CRAN-R.oo 
Requires:         R-CRAN-e1071 
Requires:         R-rpart 
Requires:         R-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-MASS 

%description
Build multivariate predictive models from large datasets having far larger
number of features than samples such as in functional genomics datasets.
Trevino and Falciani (2006) <doi:10.1093/bioinformatics/btl074>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
