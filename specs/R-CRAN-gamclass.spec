%global packname  gamclass
%global packver   0.58
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.58
Release:          1%{?dist}
Summary:          Functions and Data for a Course on Modern Regression andClassification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-car 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-DAAG 
BuildRequires:    R-MASS 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-methods 
Requires:         R-CRAN-car 
Requires:         R-mgcv 
Requires:         R-CRAN-DAAG 
Requires:         R-MASS 
Requires:         R-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-ape 
Requires:         R-KernSmooth 
Requires:         R-methods 

%description
Functions and data are provided that support a course that emphasizes
statistical issues of inference and generalizability.  Attention is
restricted to a relatively small number of methods, often (misleadingly,
in my view) referred to as algorithms.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
