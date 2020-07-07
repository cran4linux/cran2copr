%global packname  FitAR
%global packver   1.94
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.94
Release:          3%{?dist}
Summary:          Subset AR Model Fitting

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.0.0
Requires:         R-core >= 2.0.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-leaps 
BuildRequires:    R-CRAN-ltsa 
BuildRequires:    R-CRAN-bestglm 
Requires:         R-lattice 
Requires:         R-CRAN-leaps 
Requires:         R-CRAN-ltsa 
Requires:         R-CRAN-bestglm 

%description
Comprehensive model building function for identification, estimation and
diagnostic checking for AR and subset AR models. Two types of subset AR
models are supported.  One family of subset AR models, denoted by ARp, is
formed by taking subet of the original AR coefficients and in the other,
denoted by ARz, subsets of the partial autocorrelations are used. The main
advantage of the ARz model is its applicability to very large order
models.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
