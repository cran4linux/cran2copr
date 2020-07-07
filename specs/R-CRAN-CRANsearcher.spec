%global packname  CRANsearcher
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          RStudio Addin for Searching Packages in CRAN Database Based onKeywords

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-lubridate 
Requires:         R-utils 

%description
One of the strengths of R is its vast package ecosystem. Indeed, R
packages extend from visualization to Bayesian inference and from spatial
analyses to pharmacokinetics (<https://cran.r-project.org/web/views/>).
There is probably not an area of quantitative research that isn't
represented by at least one R package. At the time of this writing, there
are more than 10,000 active CRAN packages. Because of this massive
ecosystem, it is important to have tools to search and learn about
packages related to your personal R needs. For this reason, we developed
an RStudio addin capable of searching available CRAN packages directly
within RStudio.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
