%global packname  BHTSpack
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          2%{?dist}
Summary:          Bayesian Multi-Plate High-Throughput Screening of Compounds

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-R2HTML >= 2.3.2
BuildRequires:    R-CRAN-xtable >= 1.8.2
Requires:         R-CRAN-R2HTML >= 2.3.2
Requires:         R-CRAN-xtable >= 1.8.2

%description
Can be used for joint identification of candidate compound hits from
multiple assays, in drug discovery. This package implements the framework
of I. D. Shterev, D. B. Dunson, C. Chan and G. D. Sempowski. "Bayesian
Multi-Plate High-Throughput Screening of Compounds", Scientific Reports
8(1):9551, 2018. This project was funded by the Division of Allergy,
Immunology, and Transplantation, National Institute of Allergy and
Infectious Diseases, National Institutes of Health, Department of Health
and Human Services, under contract No. HHSN272201400054C entitled
"Adjuvant Discovery For Vaccines Against West Nile Virus and Influenza",
awarded to Duke University and lead by Drs. Herman Staats and Soman
Abraham.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
