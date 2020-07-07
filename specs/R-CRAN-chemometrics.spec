%global packname  chemometrics
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          3%{?dist}
Summary:          Multivariate Statistical Analysis in Chemometrics

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-MASS 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-som 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-mclust 
Requires:         R-rpart 
Requires:         R-class 
Requires:         R-CRAN-e1071 
Requires:         R-MASS 
Requires:         R-nnet 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-som 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-mclust 

%description
R companion to the book "Introduction to Multivariate Statistical Analysis
in Chemometrics" written by K. Varmuza and P. Filzmoser (2009).

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
