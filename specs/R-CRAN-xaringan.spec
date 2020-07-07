%global packname  xaringan
%global packver   0.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.16
Release:          3%{?dist}
Summary:          Presentation Ninja

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr >= 1.21
BuildRequires:    R-CRAN-xfun >= 0.6
BuildRequires:    R-CRAN-servr >= 0.13
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr >= 1.21
Requires:         R-CRAN-xfun >= 0.6
Requires:         R-CRAN-servr >= 0.13
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rmarkdown 

%description
Create HTML5 slides with R Markdown and the JavaScript library 'remark.js'
(<https://remarkjs.com>).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
