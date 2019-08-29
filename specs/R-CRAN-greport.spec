%global packname  greport
%global packver   0.7-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Graphical Reporting for Clinical Trials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rms >= 4.4.1
BuildRequires:    R-CRAN-Hmisc >= 3.17.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-survival 
BuildRequires:    R-methods 
Requires:         R-CRAN-rms >= 4.4.1
Requires:         R-CRAN-Hmisc >= 3.17.0
Requires:         R-CRAN-data.table 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Formula 
Requires:         R-survival 
Requires:         R-methods 

%description
Contains many functions useful for monitoring and reporting the results of
clinical trials and other experiments in which treatments are compared.
LaTeX is used to typeset the resulting reports, recommended to be in the
context of 'knitr'. The 'Hmisc', 'ggplot2', and 'lattice' packages are
used by 'greport' for high-level graphics.

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
%doc %{rlibdir}/%{packname}/feh.bib
%doc %{rlibdir}/%{packname}/greport.sty
%{rlibdir}/%{packname}/INDEX
