%global packname  SDAR
%global packver   0.9-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}
Summary:          Stratigraphic Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-linbin 
BuildRequires:    R-CRAN-grImport2 
BuildRequires:    R-CRAN-readxl 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-linbin 
Requires:         R-CRAN-grImport2 
Requires:         R-CRAN-readxl 

%description
A fast, consistent tool for plotting and facilitating the analysis of
stratigraphic and sedimentological data. Taking advantage of the flexible
plotting tools available in R, 'SDAR' uses stratigraphic and
sedimentological data to produce detailed graphic logs for outcrop
sections and borehole logs. These logs can include multiple features
(e.g., bed thickness, lithology, samples, sedimentary structures, colors,
fossil content, bioturbation index, electrical logs) (Johnson, 1992, <ISSN
0037-0738>).

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
%{rlibdir}/%{packname}/demo_data_entry
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
