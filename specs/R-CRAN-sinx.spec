%global packname  sinx
%global packver   0.0.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.13
Release:          3%{?dist}
Summary:          Sino Xmen Said

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-cowsay 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xaringan 
BuildRequires:    R-CRAN-pagedown 
BuildRequires:    R-CRAN-bookdownplus 
BuildRequires:    R-CRAN-rosr 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-multicolor 
BuildRequires:    R-CRAN-rmsfact 
BuildRequires:    R-CRAN-clipr 
Requires:         R-utils 
Requires:         R-CRAN-cowsay 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xaringan 
Requires:         R-CRAN-pagedown 
Requires:         R-CRAN-bookdownplus 
Requires:         R-CRAN-rosr 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-multicolor 
Requires:         R-CRAN-rmsfact 
Requires:         R-CRAN-clipr 

%description
Displays a pseudorandom message from a database of quotations. It works as
an advanced version of the package 'fortunes', while 'sinx' supports
multi-byte languages such as Chinese. The databases of 'sinx' can be given
in markdown format, which is easier and more friendly than spread sheets
for users.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/sinxs
%{rlibdir}/%{packname}/INDEX
