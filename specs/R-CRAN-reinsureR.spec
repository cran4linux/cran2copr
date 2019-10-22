%global packname  reinsureR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Reinsurance Treaties Application

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2
Requires:         R-core >= 2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Application of reinsurance treaties to claims portfolios. The package
creates a class Claims whose objective is to store claims and premiums, on
which different treaties can be applied. A statistical analysis can then
be applied to measure the impact of reinsurance, producing a table or
graphical output. This package can be used for estimating the impact of
reinsurance on several portfolios or for pricing treaties through
statistical analysis. Documentation for the implemented methods can be
found in "Reinsurance: Actuarial and Statistical Aspects" by Hansjöerg
Albrecher, Jan Beirlant, Jozef L. Teugels (2017, ISBN: 978-0-470-77268-3)
and "REINSURANCE: A Basic Guide to Facultative and Treaty Reinsurance" by
Munich Re (2010)
<https://www.munichre.com/site/mram/get/documents_E96160999/mram/assetpool.mr_america/PDFs/3_Publications/reinsurance_basic_guide.pdf>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
