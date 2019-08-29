%global packname  moveHMM
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Animal Movement Modelling using Hidden Markov Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-boot 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggmap 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-Rcpp 
Requires:         R-boot 
Requires:         R-MASS 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggmap 
Requires:         R-CRAN-numDeriv 

%description
Provides tools for animal movement modelling using hidden Markov models.
These include processing of tracking data, fitting hidden Markov models to
movement data, visualization of data and fitted model, decoding of the
state process...

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
