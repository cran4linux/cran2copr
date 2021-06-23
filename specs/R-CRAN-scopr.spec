%global __brp_check_rpaths %{nil}
%global packname  scopr
%global packver   0.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Read Ethoscope Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.00
Requires:         R-core >= 3.00
BuildArch:        noarch
BuildRequires:    R-CRAN-behavr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-behavr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-memoise 

%description
Handling of behavioural data from the Ethoscope platform (Geissmann,
Garcia Rodriguez, Beckwith, French, Jamasb and Gilestro (2017)
<DOI:10.1371/journal.pbio.2003026>). Ethoscopes
(<http://gilestrolab.github.io/ethoscope/>) are an open source/open
hardware framework made of interconnected raspberry pis
(<https://www.raspberrypi.org>) designed to quantify the behaviour of
multiple small animals in a distributed and real-time fashion. The default
tracking algorithm records primary variables such as xy coordinates,
dimensions and speed. This package is part of the rethomics framework
<http://rethomics.github.io/>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
