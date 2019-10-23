%global packname  trtf
%global packver   0.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}
Summary:          Transformation Trees and Forests

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partykit >= 1.2.1
BuildRequires:    R-CRAN-mlt >= 1.0.2
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-variables 
BuildRequires:    R-CRAN-libcoin 
BuildRequires:    R-utils 
Requires:         R-CRAN-partykit >= 1.2.1
Requires:         R-CRAN-mlt >= 1.0.2
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-sandwich 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-CRAN-variables 
Requires:         R-CRAN-libcoin 
Requires:         R-utils 

%description
Recursive partytioning of transformation models with corresponding random
forest for conditional transformation models as described in
'Transformation Forests' (Hothorn and Zeileis, 2017, <arXiv:1701.02110>)
and 'Top-Down Transformation Choice' (Hothorn, 2018,
<DOI:10.1177/1471082X17748081>).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/BMI_artificial.rda
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/ordinal_forests
%doc %{rlibdir}/%{packname}/sim
%doc %{rlibdir}/%{packname}/survival_forests
%{rlibdir}/%{packname}/INDEX
