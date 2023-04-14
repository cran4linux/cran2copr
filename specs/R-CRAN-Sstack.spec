%global __brp_check_rpaths %{nil}
%global packname  Sstack
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bootstrap Stacking of Random Forest Models for HeterogeneousData

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Generates and predicts a set of linearly stacked Random Forest models
using bootstrap sampling. Individual datasets may be heterogeneous (not
all samples have full sets of features). Contains support for
parallelization but the user should register their cores before running.
This is an extension of the method found in Matlock (2018)
<doi:10.1186/s12859-018-2060-2>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
