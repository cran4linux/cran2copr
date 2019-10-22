%global packname  mschart
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Chart Generation for 'Microsoft Word' and 'Microsoft PowerPoint'Documents

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.0
BuildRequires:    R-CRAN-officer >= 0.2.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-cellranger 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-xml2 >= 1.1.0
Requires:         R-CRAN-officer >= 0.2.0
Requires:         R-stats 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-cellranger 
Requires:         R-CRAN-writexl 
Requires:         R-grDevices 
Requires:         R-CRAN-htmltools 

%description
Create native charts for 'Microsoft PowerPoint' and 'Microsoft Word'
documents. These can then be edited and annotated. Functions are provided
to let users create charts, modify and format their content. The chart's
underlying data is automatically saved within the 'Word' document or
'PowerPoint' presentation. It extends package 'officer' that does not
contain any feature for 'Microsoft' native charts production.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/template
%{rlibdir}/%{packname}/INDEX
