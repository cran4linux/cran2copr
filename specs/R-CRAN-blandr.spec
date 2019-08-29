%global packname  blandr
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Bland-Altman Method Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.8.5
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-jmvcore >= 0.8.5
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rmarkdown 

%description
Carries out Bland Altman analyses (also known as a Tukey mean-difference
plot) as described by JM Bland and DG Altman in 1986
<doi:10.1016/S0140-6736(86)90837-8>. This package was created in 2015 as
existing Bland-Altman analysis functions did not calculate confidence
intervals. This package was created to rectify this, and create
reproducible plots. This package is also available as a module for the
'jamovi' statistical spreadsheet (see <https://www.jamovi.org> for more
information).

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
%doc %{rlibdir}/%{packname}/blandr_report_template.Rmd
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
