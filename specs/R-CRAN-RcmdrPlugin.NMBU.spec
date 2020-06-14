%global packname  RcmdrPlugin.NMBU
%global packver   1.8.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.11
Release:          2%{?dist}
Summary:          R Commander Plug-in for University Level Applied Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.1.7
BuildRequires:    R-CRAN-mixlm >= 1.2.3
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-phia 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-Rcmdr >= 2.1.7
Requires:         R-CRAN-mixlm >= 1.2.3
Requires:         R-MASS 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-phia 
Requires:         R-tcltk 
Requires:         R-CRAN-car 

%description
An R Commander "plug-in" extending functionality of linear models and
providing an interface to Partial Least Squares Regression and Linear and
Quadratic Discriminant analysis. Several statistical summaries are
extended, predictions are offered for additional types of analyses, and
extra plots, tests and mixed models are available.

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
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
