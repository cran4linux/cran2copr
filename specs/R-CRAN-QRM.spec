%global packname  QRM
%global packver   0.4-13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.13
Release:          1%{?dist}
Summary:          Provides R-Language Code to Examine Quantitative Risk ManagementConcepts

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-mgcv 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-timeDate 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-CRAN-gsl 
Requires:         R-Matrix 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-timeSeries 
Requires:         R-mgcv 
Requires:         R-methods 
Requires:         R-CRAN-timeDate 

%description
Accompanying package to the book Quantitative Risk Management: Concepts,
Techniques and Tools by Alexander J. McNeil, Rüdiger Frey, and Paul
Embrechts.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/TODO.org
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
