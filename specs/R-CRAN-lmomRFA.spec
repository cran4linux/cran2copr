%global packname  lmomRFA
%global packver   3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3
Release:          2%{?dist}
Summary:          Regional Frequency Analysis using L-Moments

License:          Common Public License Version 1.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-lmom >= 2.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-lmom >= 2.0
Requires:         R-stats 
Requires:         R-graphics 

%description
Functions for regional frequency analysis using the methods of J. R. M.
Hosking and J. R. Wallis (1997), "Regional frequency analysis: an approach
based on L-moments".

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
%doc %{rlibdir}/%{packname}/lmomRFA-manual.pdf
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
