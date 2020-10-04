%global packname  CondIndTests
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Nonlinear Conditional Independence Tests

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-quantregForest 
BuildRequires:    R-CRAN-lawstat 
BuildRequires:    R-CRAN-RPtests 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-mgcv 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-mize 
Requires:         R-methods 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-quantregForest 
Requires:         R-CRAN-lawstat 
Requires:         R-CRAN-RPtests 
Requires:         R-CRAN-caTools 
Requires:         R-mgcv 
Requires:         R-MASS 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-mize 

%description
Code for a variety of nonlinear conditional independence tests: Kernel
conditional independence test (Zhang et al., UAI 2011, <arXiv:1202.3775>),
Residual Prediction test (based on Shah and Buehlmann,
<arXiv:1511.03334>), Invariant environment prediction, Invariant target
prediction, Invariant residual distribution test, Invariant conditional
quantile prediction (all from Heinze-Deml et al., <arXiv:1706.08576>).

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
