%global packname  ck37r
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Chris Kennedy's R Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cvAUC 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-h2o 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-precrec 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-reader 
BuildRequires:    R-CRAN-RhpcBLASctl 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-CRAN-rpart.plot 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-tmle 
BuildRequires:    R-CRAN-weights 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cvAUC 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-h2o 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-precrec 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-reader 
Requires:         R-CRAN-RhpcBLASctl 
Requires:         R-CRAN-ROCR 
Requires:         R-CRAN-rpart.plot 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-tmle 
Requires:         R-CRAN-weights 

%description
Toolkit for statistical, machine learning, and targeted learning analyses.
Functionality includes loading & auto-installing packages, standardizing
datasets, creating missingness indicators, imputing missing values,
creating multicore or multinode clusters, automatic SLURM integration,
enhancing SuperLearner and TMLE with automatic parallelization, and many
other SuperLearner analysis & plotting enhancements.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
