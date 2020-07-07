%global packname  confidence
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Confidence Estimation of Environmental State Classifications

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-tcltk 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 

%description
Functions for estimating and reporting multi-year averages and
corresponding confidence intervals and distributions. A potential use case
is reporting the chemical and ecological status of surface waters
according to the European Water Framework Directive.

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
%doc %{rlibdir}/%{packname}/css
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/Rmd
%{rlibdir}/%{packname}/INDEX
