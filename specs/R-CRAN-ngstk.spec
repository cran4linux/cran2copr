%global packname  ngstk
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Next-Generation Sequencing (NGS) Data Analysis Toolkit

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-configr >= 0.3.1
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-parallel 
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-configr >= 0.3.1
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-future 
Requires:         R-CRAN-optparse 
Requires:         R-parallel 

%description
Can be used to facilitate the analysis of NGS data, such as visualization,
conversion of data format for WEB service input and other purpose.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
