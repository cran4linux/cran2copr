%global packname  define
%global packver   0.2.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          2%{?dist}
Summary:          Create FDA-Style Data and Program Definitions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-SASxport 
BuildRequires:    R-CRAN-encode 
BuildRequires:    R-CRAN-spec 
BuildRequires:    R-CRAN-latexpdf 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-SASxport 
Requires:         R-CRAN-encode 
Requires:         R-CRAN-spec 
Requires:         R-CRAN-latexpdf 

%description
Creates a directory of archived files with a descriptive 'PDF' document at
the root level (i.e. 'define.pdf') containing tables of definitions of
data items and relative-path hyperlinks to the documented files. Converts
file extensions to 'txt' per FDA expectations and converts 'CSV' files to
'SAS' Transport format. Relies on data item descriptors stored as per R
package 'spec'. See 'package?define'. See also '?define'. Requires a
compatible installation of 'pdflatex', e.g. <https://miktex.org/>.

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
%doc %{rlibdir}/%{packname}/define.pdf
%doc %{rlibdir}/%{packname}/logo.pdf
%doc %{rlibdir}/%{packname}/minimal.pdf
%doc %{rlibdir}/%{packname}/poster.pdf
%{rlibdir}/%{packname}/INDEX
