%global packname  GRPtests
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Goodness-of-Fit Tests in High-Dimensional GLMs

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RPtests 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForest 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-RPtests 

%description
Methodology for testing nonlinearity in the conditional mean function in
low- or high-dimensional generalized linear models, and the significance
of (potentially large) groups of predictors. Details on the algorithms can
be found in the paper by Jankova, Shah, Buehlmann and Samworth (2019)
<arXiv:1908.03606>.

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
