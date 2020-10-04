%global packname  gifti
%global packver   0.7.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          3%{?dist}%{?buildtag}
Summary:          Reads in 'Neuroimaging' 'GIFTI' Files with Geometry Information

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.1.1
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-tools 
Requires:         R-CRAN-xml2 >= 1.1.1
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-R.utils 
Requires:         R-tools 

%description
Functions to read in the geometry format under the 'Neuroimaging'
'Informatics' Technology Initiative ('NIfTI'), called 'GIFTI'
<https://www.nitrc.org/projects/gifti/>. These files contain surfaces of
brain imaging data.

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
%{rlibdir}/%{packname}/INDEX
