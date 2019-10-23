%global packname  ExPanDaR
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Explore Panel Data Interactively

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-lfe 
BuildRequires:    R-CRAN-multiwayvcov 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-stargazer 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-shinycssloaders 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-rio 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-lfe 
Requires:         R-CRAN-multiwayvcov 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-stargazer 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-shinycssloaders 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-rio 

%description
Provides a shiny-based front end (the 'ExPanD' app) and a set of functions
for exploratory panel data analysis. Run as a web-based app, 'ExPanD'
enables users to assess the robustness of empirical evidence without
providing them access to the underlying data. You can also use the
functions of the package to support your exploratory data analysis
workflow. Refer to the vignettes of the package for more information on
how to use 'ExPanD' and/or the functions of this package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/application
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
