%global packname  SCtools
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Extensions for Synthetic Controls Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.6.2
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Synth 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-future >= 1.6.2
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Synth 
Requires:         R-CRAN-stringr 
Requires:         R-stats 
Requires:         R-CRAN-cvTools 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 

%description
Extensions to the synthetic controls analyses performed by the package
'Synth' as detailed in Abadie, Diamond, and Hainmueller (2011)
<doi:10.18637/jss.v042.i13>. Includes generating and plotting placebos,
post/pre-MSPE (mean squared prediction error) significance tests and
plots, and calculating average treatment effects for multiple treated
units. This package represents an implementation of those methods
suggested in Abadie, Diamond,and Hainmueller (2010)
<doi:10.1198/jasa.2009.ap08746> for use in synthetic control analysis.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/paper.bib
%doc %{rlibdir}/%{packname}/paper.html
%doc %{rlibdir}/%{packname}/paper.md
%doc %{rlibdir}/%{packname}/unnamed-chunk-8-1.png
%{rlibdir}/%{packname}/INDEX
