%global __brp_check_rpaths %{nil}
%global packname  pipe.design
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          3%{?dist}%{?buildtag}
Summary:          Dual-Agent Dose Escalation for Phase I Trials using the PIPEDesign

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-xtable 

%description
Implements the Product of Independent beta Probabilities dose Escalation
(PIPE) design for dual-agent Phase I trials as described in Mander AP,
Sweeting MJ (2015) <DOI:10.1002/sim.6434>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/citation
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
