%global packname  reverseR
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          2%{?dist}
Summary:          Linear Regression Stability to Significance Reversal

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-DT 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-DT 

%description
Tests linear regressions for significance reversal through
leave-one(multiple)-out and shifting/addition of response values. The
paradigm of the package is loosely based on the somewhat forgotten
"dfstat" criterion (Belsley, Kuh & Welsch 1980
<doi:10.1002/0471725153.ch2>), which tests influential values in linear
models from their effect on statistical inference, i.e. changes in
p-value.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/reverseR
%{rlibdir}/%{packname}/INDEX
