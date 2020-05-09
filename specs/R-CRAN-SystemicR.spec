%global packname  SystemicR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Monitoring Systemic Risk

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-xts 

%description
The past decade has demonstrated an increased need to better understand
risks leading to systemic crises. This framework offers scholars,
practitioners and policymakers a useful toolbox to explore such risks in
financial systems. Specifically, this framework provides popular
econometric and network measures to monitor systemic risk and to measure
the consequences of regulatory decisions. These systemic risk measures are
based on the frameworks of Adrian and Brunnermeier (2016)
<doi:10.1257/aer.20120555> and Billio, Getmansky, Lo and Pelizzon (2012)
<doi:10.1016/j.jfineco.2011.12.010>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
