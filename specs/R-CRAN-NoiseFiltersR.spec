%global packname  NoiseFiltersR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Label Noise Filters for Data Preprocessing in Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RWeka 
BuildRequires:    R-CRAN-kknn 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RWeka 
Requires:         R-CRAN-kknn 
Requires:         R-nnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-MASS 
Requires:         R-CRAN-rJava 
Requires:         R-stats 
Requires:         R-utils 

%description
An extensive implementation of state-of-the-art and classical algorithms
to preprocess label noise in classification problems.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
