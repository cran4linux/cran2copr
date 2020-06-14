%global packname  xplorerr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Tools for Interactive Data Exploration

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-shiny 
Requires:         R-utils 

%description
Tools for interactive data exploration built using 'shiny'. Includes apps
for descriptive statistics, visualizing probability distributions,
inferential statistics, linear regression, logistic regression and RFM
analysis.

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
%doc %{rlibdir}/%{packname}/app-blorr
%doc %{rlibdir}/%{packname}/app-descriptr
%doc %{rlibdir}/%{packname}/app-inferr
%doc %{rlibdir}/%{packname}/app-olsrr
%doc %{rlibdir}/%{packname}/app-rfm
%doc %{rlibdir}/%{packname}/app-vistributions
%doc %{rlibdir}/%{packname}/app-visualize
%{rlibdir}/%{packname}/INDEX
