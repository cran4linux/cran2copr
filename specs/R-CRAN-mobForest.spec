%global packname  mobForest
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Model Based Random Forest Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-sandwich >= 2.4.0
BuildRequires:    R-CRAN-zoo >= 1.8.0
BuildRequires:    R-CRAN-strucchange >= 1.5.1
BuildRequires:    R-CRAN-party >= 1.2.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-modeltools 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-sandwich >= 2.4.0
Requires:         R-CRAN-zoo >= 1.8.0
Requires:         R-CRAN-strucchange >= 1.5.1
Requires:         R-CRAN-party >= 1.2.4
Requires:         R-methods 
Requires:         R-CRAN-modeltools 
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions to implements random forest method for model based recursive
partitioning. The mob() function, developed by Zeileis et al. (2008),
within 'party' package, is modified to construct model-based decision
trees based on random forests methodology. The main input function
mobforest.analysis() takes all input parameters to construct trees,
compute out-of-bag errors, predictions, and overall accuracy of forest.
The algorithm performs parallel computation using cluster functions within
'parallel' package.

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
%{rlibdir}/%{packname}/INDEX
