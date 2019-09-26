%global packname  VSURF
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Variable Selection Using Random Forests

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rborist 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-rpart 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-Rborist 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-rpart 

%description
Three steps variable selection procedure based on random forests.
Initially developed to handle high dimensional data (for which number of
variables largely exceeds number of observations), the package is very
versatile and can treat most dimensions of data, for regression and
supervised classification problems. First step is dedicated to eliminate
irrelevant variables from the dataset. Second step aims to select all
variables related to the response for interpretation purpose. Third step
refines the selection by eliminating redundancy in the set of variables
selected by the second step, for prediction purpose. Genuer, R. Poggi,
J.-M. and Tuleau-Malot, C. (2015)
<https://journal.r-project.org/archive/2015-2/genuer-poggi-tuleaumalot.pdf>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
