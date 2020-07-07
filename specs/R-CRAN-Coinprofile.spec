%global packname  Coinprofile
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}
Summary:          Coincident Profile

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 1.0.1
BuildRequires:    R-CRAN-exactRankTests >= 0.8.29
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-CRAN-ggplot2 >= 1.0.1
Requires:         R-CRAN-exactRankTests >= 0.8.29
Requires:         R-CRAN-zoo 
Requires:         R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-Rdpack 

%description
Builds the coincident profile proposed by Martinez, W and Nieto, Fabio H
and Poncela, P (2016) <doi:10.1016/j.spl.2015.11.008>. This methodology
studies the relationship between a couple of time series based on the the
set of turning points of each time series. The coincident profile
establishes if two time series are coincident, or one of them leads the
second.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
