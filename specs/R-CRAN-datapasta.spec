%global packname  datapasta
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          2%{?dist}
Summary:          R Tools for Data Copy-Pasta

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-readr >= 1.2.0
BuildRequires:    R-CRAN-rstudioapi >= 0.6
BuildRequires:    R-CRAN-clipr >= 0.3.0
BuildRequires:    R-methods 
Requires:         R-CRAN-readr >= 1.2.0
Requires:         R-CRAN-rstudioapi >= 0.6
Requires:         R-CRAN-clipr >= 0.3.0
Requires:         R-methods 

%description
RStudio addins and R functions that make copy-pasting vectors and tables
to text painless.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/media
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
