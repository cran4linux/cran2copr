%global packname  DTAT
%global packver   0.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          2%{?dist}
Summary:          Dose Titration Algorithm Tuning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-km.ci 
BuildRequires:    R-CRAN-pomp 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-r2d3 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
Requires:         R-survival 
Requires:         R-CRAN-km.ci 
Requires:         R-CRAN-pomp 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-r2d3 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 

%description
Dose Titration Algorithm Tuning (DTAT) is a methodologic framework
allowing dose individualization to be conceived as a continuous learning
process that begins in early-phase clinical trials and continues
throughout drug development, on into clinical practice. This package
includes code that researchers may use to reproduce or extend key results
of the DTAT research programme, plus tools for trialists to design and
simulate a '3+3/PC' dose-finding study. Please see Norris (2017)
<doi:10.12688/f1000research.10624.3> and Norris (2017)
<doi:10.1101/240846>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/shiny-apps
%{rlibdir}/%{packname}/INDEX
