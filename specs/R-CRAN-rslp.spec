%global packname  rslp
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}
Summary:          A Stemming Algorithm for the Portuguese Language

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tokenizers 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tokenizers 

%description
Implements the "Stemming Algorithm for the Portuguese Language"
<DOI:10.1109/SPIRE.2001.10024>.

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
%doc %{rlibdir}/%{packname}/steprules.rds
%doc %{rlibdir}/%{packname}/steprules.txt
%{rlibdir}/%{packname}/INDEX
