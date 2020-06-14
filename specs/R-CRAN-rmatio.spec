%global packname  rmatio
%global packver   0.14.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.0
Release:          2%{?dist}
Summary:          Read and Write 'Matlab' Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
Requires:         zlib
BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-utils 

%description
Read and write 'Matlab' MAT files from R. The 'rmatio' package supports
reading MAT version 4, MAT version 5 and MAT compressed version 5. The
'rmatio' package can write version 5 MAT files and version 5 files with
variable compression.

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
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/NOTICE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
