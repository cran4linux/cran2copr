%global packname  BootstrapQTL
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Bootstrap cis-QTL Method that Corrects for the Winner's Curse

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MatrixEQTL 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-MatrixEQTL 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 

%description
Identifies genome-related molecular traits with significant evidence of
genetic regulation and performs a bootstrap procedure to correct estimated
effect sizes for over-estimation present in cis-QTL mapping studies (The
"Winner's Curse"), described in Huang QQ *et al.* 2018 <doi:
10.1093/nar/gky780>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
