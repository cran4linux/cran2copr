%global __brp_check_rpaths %{nil}
%global packname  cordillera
%global packver   0.8-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculation of the OPTICS Cordillera

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-yesno 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-yesno 

%description
Functions for calculating the OPTICS Cordillera. The OPTICS Cordillera
measures the amount of 'clusteredness' in a numeric data matrix within a
distance-density based framework for a given minimum number of points
comprising a cluster, as described in Rusch, Hornik, Mair (2017)
<doi:10.1080/10618600.2017.1349664>. There is an R native version and a
version that uses 'ELKI', with methods for printing, summarizing, and
plotting the result. There also is an interface to the reference
implementation of OPTICS in 'ELKI'.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
