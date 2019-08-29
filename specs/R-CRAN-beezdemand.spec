%global packname  beezdemand
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Behavioral Economic Easy Demand

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5
Requires:         R-core >= 2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nlmrt 
BuildRequires:    R-CRAN-nlstools 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
Requires:         R-CRAN-nlmrt 
Requires:         R-CRAN-nlstools 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 

%description
Facilitates many of the analyses performed in studies of behavioral
economic demand. The package supports commonly-used options for modeling
operant demand including (1) data screening proposed by Stein, Koffarnus,
Snider, Quisenberry, & Bickel (2015; <doi:10.1037/pha0000020>), (2)
fitting models of demand such as linear (Hursh, Raslear, Bauman, & Black,
1989, <doi:10.1007/978-94-009-2470-3_22>), exponential (Hursh &
Silberberg, 2008, <doi:10.1037/0033-295X.115.1.186>) and modified
exponential (Koffarnus, Franck, Stein, & Bickel, 2015,
<doi:10.1037/pha0000045>), and (3) calculating numerous measures relevant
to applied behavioral economists (Intensity, Pmax, Omax). Also supports
plotting and comparing data.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
