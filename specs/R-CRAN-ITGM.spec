%global packname  ITGM
%global packver   0.41
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.41
Release:          2%{?dist}
Summary:          Individual Tree Growth Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Fgmutils >= 0.8
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-sqldf 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-Fgmutils >= 0.8
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-sqldf 
Requires:         R-CRAN-plyr 

%description
Individual tree model is an instrument to support the decision with regard
to forest management. This package provides functions that let you work
with data for this model. Also other support functions and extension
related to this model are available.

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
