%global __brp_check_rpaths %{nil}
%global packname  gnumeric
%global packver   0.7-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.8
Release:          3%{?dist}%{?buildtag}
Summary:          Read Data from Files Readable by 'gnumeric'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.8.1
Requires:         R-core >= 2.8.1
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-utils 
Requires:         R-CRAN-XML 
Requires:         R-utils 

%description
Read data files readable by 'gnumeric' into 'R'. Can read whole sheet or a
range, from several file formats, including the native format of
'gnumeric'. Reading is done by using 'ssconvert' (a file converter utility
included in the 'gnumeric' distribution
<http://projects.gnome.org/gnumeric/>) to convert the requested part to
CSV. From 'gnumeric' files (but not other formats) can list sheet names
and sheet sizes or read all sheets.

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
%{rlibdir}/%{packname}/INDEX
