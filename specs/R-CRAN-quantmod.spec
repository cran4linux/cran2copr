%global packname  quantmod
%global packver   0.4-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.16
Release:          1%{?dist}
Summary:          Quantitative Financial Modelling Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xts >= 0.9.0
BuildRequires:    R-CRAN-TTR >= 0.2
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
Requires:         R-CRAN-xts >= 0.9.0
Requires:         R-CRAN-TTR >= 0.2
Requires:         R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-CRAN-curl 

%description
Specify, build, trade, and analyse quantitative financial trading
strategies.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
