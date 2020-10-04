%global packname  SMPracticals
%global packver   1.4-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Practicals for Use with Davison (2003) Statistical Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 1.14.0
Requires:         R-core >= 1.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-MASS 
BuildRequires:    R-nlme 
BuildRequires:    R-survival 
Requires:         R-CRAN-ellipse 
Requires:         R-MASS 
Requires:         R-nlme 
Requires:         R-survival 

%description
Contains the datasets and a few functions for use with the practicals
outlined in Appendix A of the book Statistical Models (Davison, 2003,
Cambridge University Press). The practicals themselves can be found at
<http://statwww.epfl.ch/davison/SM/>.

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
%{rlibdir}/%{packname}/INDEX
