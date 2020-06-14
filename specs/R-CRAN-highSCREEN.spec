%global packname  highSCREEN
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          2%{?dist}
Summary:          High-Throughput Screening for Plate Based Assays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots >= 3.0.1
Requires:         R-CRAN-gplots >= 3.0.1

%description
Can be used to carry out extraction, normalization, quality control (QC),
candidate hits identification and visualization for plate based assays, in
drug discovery. This project was funded by the Division of Allergy,
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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
