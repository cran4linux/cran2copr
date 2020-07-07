%global packname  QCAtools
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Helper Functions for QCA in R

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-directlabels >= 2013.6.15
BuildRequires:    R-CRAN-QCA >= 2.5
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3.1
BuildRequires:    R-CRAN-stringr >= 0.6.2
BuildRequires:    R-graphics 
Requires:         R-CRAN-directlabels >= 2013.6.15
Requires:         R-CRAN-QCA >= 2.5
Requires:         R-CRAN-ggplot2 >= 0.9.3.1
Requires:         R-CRAN-stringr >= 0.6.2
Requires:         R-graphics 

%description
Helper functions for Qualitative Comparative Analysis: evaluate and plot
Boolean formulae on fuzzy set score data, apply Boolean operations,
compute consistency and coverage measures.

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
