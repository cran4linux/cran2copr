%global packname  r4ss
%global packver   1.36.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.36.1
Release:          3%{?dist}
Summary:          R Code for Stock Synthesis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-kableExtra 

%description
A collection of R functions for use with Stock Synthesis, a fisheries
stock assessment modeling platform written in ADMB by Dr. Richard D.
Methot at the NOAA Northwest Fisheries Science Center. The functions
include tools for summarizing and plotting results, manipulating files,
visualizing model parameterizations, and various other common stock
assessment tasks.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Shiny
%{rlibdir}/%{packname}/INDEX
