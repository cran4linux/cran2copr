%global packname  CADStat
%global packver   3.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.8
Release:          1%{?dist}
Summary:          Provides a GUI to Several Statistical Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-JGR >= 1.7.10
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-bio.infer 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gmodels 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-JavaGD 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-MASS 
Requires:         R-CRAN-JGR >= 1.7.10
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-XML 
Requires:         R-lattice 
Requires:         R-CRAN-bio.infer 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gmodels 
Requires:         R-CRAN-quantreg 
Requires:         R-rpart 
Requires:         R-CRAN-JavaGD 
Requires:         R-CRAN-car 
Requires:         R-MASS 

%description
Using Java GUI for R (JGR), CADStat provides a user interface for several
statistical methods - scatterplot, boxplot, linear regression, generalized
linear regression, quantile regression, conditional probability
calculations, and regression trees.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/menu
%{rlibdir}/%{packname}/INDEX
